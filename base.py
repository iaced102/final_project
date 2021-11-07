import jwt
import requests
import json
import datetime
from time import time
from classroom.models import ClassRoom, Time_Session
from sessions.models import Session

'''
7GkaJatXS0CapfgAHSxJPA
DsItxIOlmTdIJtNLbpL3NPOpjz3ea36TW6Lt
eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJITlBCQ004dlFTLUt0VU1JTjlYaE1RIn0.q2hAghrFFXrLmSmSikZC1KIxk40sm0k5CFAd8YSumeY
eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IjdHa2FKYXRYUzBDYXBmZ0FIU3hKUEEiLCJleHAiOjE2MzU1MjQ4MzIsImlhdCI6MTYzNTQzODQzNX0.CMLFx9lRB20qIhTLZfNJHjWmHuk6T3jY4lC8Hy0DwOY
'''
'''
hInu8hLOSreg9mVtJEl3ww
mPlTDoia4tV1824BZCpoANAbJ43OCdkSgI73
'''
# Enter your API key and your API secret
API_KEY = '7GkaJatXS0CapfgAHSxJPA'
API_SEC = 'DsItxIOlmTdIJtNLbpL3NPOpjz3ea36TW6Lt'

# create a function to generate a token
# using the pyjwt library
def generateToken():
	token = jwt.encode(
		
		# Create a payload of the token containing
		# API Key & expiration time
		{'iss': API_KEY, 'exp': time() + 5000},
		
		# Secret used to generate token signature
		API_SEC,
		
		# Specify the hashing alg
		algorithm='HS256'
	)
	return token


# create json data for post requests
meetingdetails = {"topic": "The title of your zoom meeting",
				"type": 2,
				"start_time": "2019-06-14T10: 21: 57",
				"duration": "45",
				"timezone": "(GMT+7:00)",
				"agenda": "test",

				"recurrence": {"type": 1,
								"repeat_interval": 1
								},
				"settings": {"host_video": "true",
							"participant_video": "true",
							"join_before_host": "False",
							"mute_upon_entry": "False",
							"watermark": "true",
							"audio": "voip",
							"auto_recording": "cloud"
							}
				}

# send a request with headers including
# a token and meeting details
def createMeeting(topic, start_time, agenda):
	meetingdetails['topic'] =topic
	meetingdetails['start_time'] =start_time
	meetingdetails['agenda'] = agenda
	headers = {'authorization': 'Bearer %s' % generateToken(),
			'content-type': 'application/json'}
	r = requests.post(
		f'https://api.zoom.us/v2/users/me/meetings',
	headers=headers, data=json.dumps(meetingdetails))

	# print(r.text)
	# converting the output into json and extracting the details
	y = json.loads(r.text)
	try:
		join_URL = y["join_url"]
		meetingPassword = y["password"]
		return {'id_meeting':y['id'],'passwords':y["password"],'join_url':y["join_url"]}
	except KeyError:
		print('khong the tao ra cuoc hop')
		


# run the create meeting function



def auto_create_sessions(classroom):
	time=[]
	time_1= classroom.start_learn
	choice_weekday = {
		'Monday':0,
		'Tuesday':1,
		'Wednesday':2,
		'Thursday':3,
		'Friday':4,
		'Saturday':5,
		'Sunday':6
	}
	for a in classroom.schedule.all():
		while time_1.weekday() != choice_weekday[a.weekday_session]:
			time_1 +=datetime.timedelta(days=1)
		time.append([time_1,a.time])
	count_time = 0
	count_session = 0
	if len(time) ==0:
		return 1
	else:
		for a in classroom.sessions.all():
			return 0
		for a in range(classroom.type.number_sessions):
			session = Session(name=f'bài {a+1} lớp {classroom.name}', date=time[count_time][0], time=time[count_time][1])
			time[count_time][0] += datetime.timedelta(days=7)
			count_time+=1
			session.save()
			if count_time == len(time):
				count_time=0
			classroom.sessions.add(session)
			classroom.save()
			


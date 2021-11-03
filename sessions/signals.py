from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver
from .models import Session
from classroom.models import ClassRoom
from base import createMeeting, generateToken
from base import auto_create_sessions

@receiver(post_save, sender=Session)
def post_save_create_session(sender, instance, created, **kwargs):
    if created:
        start_time = str(instance.date) +'T7: ' + str(instance.time)
        zoom = createMeeting(instance.name, start_time, instance.name)
        try:
            instance.link_zoom = zoom['join_url']
            instance.id_meeting= zoom['id_meeting']
            instance.password_meeting = zoom['passwords']
            instance.save()
        except TypeError:
            print('khong the tao ra cuoc hop')
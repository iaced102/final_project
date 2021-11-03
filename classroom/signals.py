from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver
from .models import Session
from classroom.models import ClassRoom, Link_Students_to_Students
from base import auto_create_sessions

@receiver(m2m_changed, sender=ClassRoom.students.through)
def m2m_changed_order(sender, instance, action, **kwargs):
    if action in ["post_add"]:
        Link_Students_to_Students.objects.create(student=instance.students.all()[len(instance.students.all()) - 1].student, to_class=instance)
        


@receiver(m2m_changed, sender=ClassRoom.schedule.through)
def m2m_changed_order(sender, instance, action, **kwargs):
    if action == 'post_add':
        auto_create_sessions(instance)
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Student

User = get_user_model()
@receiver(post_save, sender=User)
def post_save_create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(student = instance)
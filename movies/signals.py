from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save, pre_delete, pre_save
from .models import *

@receiver(post_save, sender=movies)
def notify_add(instance, *args, **kwargs):
    send_mail(
        subject='New Movie Notify',
        message=f"Dear User {instance.title} just has been added to our movies library you can view it at \n http://localhost:8000/movies/{instance.id}/details",
        from_email='saiednotifier@gmail.com',
        recipient_list=['ahmed.saeed311294@gmail.com'],
        fail_silently=True
    )
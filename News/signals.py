from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
import datetime

from News.models import *
from News.tasks import send_notify_new_post
from NewsPortal import settings


@receiver(m2m_changed, sender=PostCategory)
def send_notify_new_post_handler(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        send_notify_new_post.delay(instance.pk)

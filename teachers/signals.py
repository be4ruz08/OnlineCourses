import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
from django.conf import settings

if not settings.configured:
    django.setup()


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from teachers.models import Teacher


@receiver(post_save, sender=Teacher)
def teacher_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'Teacher {instance.full_name} created.')
    else:
        print(f'Teacher {instance.full_name} updated.')


@receiver(post_delete, sender=Teacher)
def teacher_post_delete(sender, instance, **kwargs):
    print(f'Teacher {instance.full_name} deleted.')


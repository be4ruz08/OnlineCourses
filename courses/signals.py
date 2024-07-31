import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
from django.conf import settings

if not settings.configured:
    django.setup()


from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from courses.models import Category, Course, Comment


@receiver(post_save, sender=Category)
def category_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'Category {instance.title} created.')
    else:
        print(f'Category {instance.title} updated.')


@receiver(post_delete, sender=Category)
def category_post_delete(sender, instance, **kwargs):
    print(f'Category {instance.title} deleted.')


@receiver(post_save, sender=Course)
def course_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'Course {instance.title} created.')
    else:
        print(f'Course {instance.title} updated.')


@receiver(post_delete, sender=Course)
def course_post_delete(sender, instance, **kwargs):
    print(f'Course {instance.title} deleted.')


@receiver(post_save, sender=Comment)
def comment_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'Comment by {instance.name} created.')
    else:
        print(f'Comment by {instance.name} updated.')


@receiver(post_delete, sender=Comment)
def comment_post_delete(sender, instance, **kwargs):
    print(f'Comment by {instance.name} deleted.')



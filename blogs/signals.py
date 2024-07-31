import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
from django.conf import settings

if not settings.configured:
    django.setup()

from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from blogs.models import Author, Blog, BlogImage


@receiver(post_save, sender=Author)
def author_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'Author {instance.full_name} created.')
    else:
        print(f'Author {instance.full_name} updated.')


@receiver(post_delete, sender=Author)
def author_post_delete(sender, instance, **kwargs):
    print(f'Author {instance.full_name} deleted.')


@receiver(post_save, sender=Blog)
def blog_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'Blog {instance.title} created.')
    else:
        print(f'Blog {instance.title} updated.')


@receiver(post_delete, sender=Blog)
def blog_post_delete(sender, instance, **kwargs):
    print(f'Blog {instance.title} deleted.')


@receiver(post_save, sender=BlogImage)
def blogimage_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'BlogImage for Blog ID {instance.blog_id.id} created.')
    else:
        print(f'BlogImage for Blog ID {instance.blog_id.id} updated.')


@receiver(post_delete, sender=BlogImage)
def blogimage_post_delete(sender, instance, **kwargs):
    print(f'BlogImage for Blog ID {instance.blog_id.id} deleted.')


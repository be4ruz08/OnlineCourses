# Generated by Django 5.0.7 on 2024-07-30 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_rename_blog_id_comment_blog_remove_comment_course_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
    ]

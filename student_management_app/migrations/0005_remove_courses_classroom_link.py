# Generated by Django 4.0.1 on 2023-10-03 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0004_remove_courses_course_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='classroom_link',
        ),
    ]
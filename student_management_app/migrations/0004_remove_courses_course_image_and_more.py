# Generated by Django 4.0.1 on 2023-10-03 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0003_courses_classroom_link_courses_course_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='course_image',
        ),
        migrations.AlterField(
            model_name='courses',
            name='classroom_link',
            field=models.URLField(blank=True, default=''),
        ),
    ]

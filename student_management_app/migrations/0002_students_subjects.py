# Generated by Django 4.0.1 on 2023-10-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='subjects',
            field=models.ManyToManyField(to='student_management_app.Subjects'),
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-06 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='user',
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-06 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0037_appointments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='userid',
        ),
    ]

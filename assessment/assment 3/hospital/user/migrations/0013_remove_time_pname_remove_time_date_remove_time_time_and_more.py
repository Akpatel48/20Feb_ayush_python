# Generated by Django 5.0.7 on 2024-08-01 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='pname',
        ),
        migrations.RemoveField(
            model_name='time',
            name='date',
        ),
        migrations.RemoveField(
            model_name='time',
            name='time',
        ),
        migrations.DeleteModel(
            name='appointments',
        ),
    ]

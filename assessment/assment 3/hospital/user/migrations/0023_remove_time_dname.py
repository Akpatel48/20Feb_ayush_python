# Generated by Django 5.0.7 on 2024-08-06 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_time_dname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='dname',
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-06 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_alter_time_dname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='appointments',
        ),
    ]

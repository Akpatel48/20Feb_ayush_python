# Generated by Django 5.0.6 on 2024-07-06 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_doctors_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='logo',
            field=models.ImageField(default='', upload_to='static/images/doctor'),
        ),
    ]

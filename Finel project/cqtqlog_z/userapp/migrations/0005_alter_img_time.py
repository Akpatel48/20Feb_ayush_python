# Generated by Django 5.0.6 on 2024-07-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_img_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='time',
            field=models.DateField(auto_now=True),
        ),
    ]

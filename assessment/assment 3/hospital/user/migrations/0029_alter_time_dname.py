# Generated by Django 5.0.7 on 2024-08-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='dname',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-10 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_doctors_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.login'),
        ),
    ]

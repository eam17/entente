# Generated by Django 3.0.5 on 2020-04-23 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_profile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
    ]

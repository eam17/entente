# Generated by Django 3.0.5 on 2020-04-23 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
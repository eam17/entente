# Generated by Django 3.0.5 on 2020-04-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

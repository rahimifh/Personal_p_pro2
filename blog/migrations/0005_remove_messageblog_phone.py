# Generated by Django 3.0.8 on 2020-08-17 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_messageblog_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageblog',
            name='phone',
        ),
    ]

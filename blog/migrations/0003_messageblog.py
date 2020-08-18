# Generated by Django 3.0.8 on 2020-08-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200731_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='messageblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogid', models.IntegerField(default=0)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('important', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('like', models.IntegerField(default=0)),
            ],
        ),
    ]
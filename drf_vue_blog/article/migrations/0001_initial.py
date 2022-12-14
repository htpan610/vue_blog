# Generated by Django 3.1.3 on 2022-09-15 22:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 9, 15, 22, 42, 34, 59819, tzinfo=utc))),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 15:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0007_auto_20160604_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 4, 15, 10, 56, 461277, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 4, 15, 11, 9, 316140, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

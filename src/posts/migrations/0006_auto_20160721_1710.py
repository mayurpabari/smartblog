# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-21 17:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20160721_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 7, 21, 17, 10, 20, 941692, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

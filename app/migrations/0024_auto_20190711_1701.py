# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-11 09:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20190711_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='xiang',
            name='oid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='manage',
            name='time',
            field=models.CharField(default=datetime.datetime(2019, 7, 11, 17, 1, 47, 334752), max_length=30),
        ),
        migrations.AlterField(
            model_name='shangp',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 17, 1, 47, 338751)),
        ),
        migrations.AlterField(
            model_name='user',
            name='regtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 17, 1, 47, 333750)),
        ),
    ]
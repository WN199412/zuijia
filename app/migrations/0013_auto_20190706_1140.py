# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-06 03:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190706_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='gid',
        ),
        migrations.RemoveField(
            model_name='size',
            name='bh',
        ),
        migrations.AddField(
            model_name='details',
            name='bh',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='size',
            name='gid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Shangp'),
        ),
        migrations.AlterField(
            model_name='manage',
            name='time',
            field=models.CharField(default=datetime.datetime(2019, 7, 6, 11, 40, 58, 353364), max_length=30),
        ),
        migrations.AlterField(
            model_name='shangp',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 11, 40, 58, 356366)),
        ),
        migrations.AlterField(
            model_name='user',
            name='regtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 11, 40, 58, 352362)),
        ),
    ]

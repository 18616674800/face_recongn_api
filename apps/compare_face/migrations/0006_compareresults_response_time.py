# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_face', '0005_auto_20180111_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='compareresults',
            name='response_time',
            field=models.CharField(default='', max_length=3000, verbose_name='响应时间'),
        ),
    ]

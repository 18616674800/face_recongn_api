# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 00:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaceSets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='人脸库名', max_length=50, verbose_name='人脸库名')),
                ('desc', models.TextField(default='', help_text='人脸库名描述', verbose_name='人脸库名描述')),
                ('active', models.BooleanField(default=True, help_text='是否激活', verbose_name='是否激活')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '人脸库',
                'verbose_name_plural': '人脸库',
            },
        ),
    ]

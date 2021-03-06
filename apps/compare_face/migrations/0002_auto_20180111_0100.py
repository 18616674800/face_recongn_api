# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compare_face', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compareresults',
            options={'verbose_name': '人脸搜索结果', 'verbose_name_plural': '人脸搜索结果'},
        ),
        migrations.AlterField(
            model_name='compareresults',
            name='related_face',
            field=models.ForeignKey(help_text='相关联人脸id', on_delete=django.db.models.deletion.CASCADE, to='faces.FaceInfo', verbose_name='相关联人脸id'),
        ),
    ]

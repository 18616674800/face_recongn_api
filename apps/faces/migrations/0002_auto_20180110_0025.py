# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 00:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faces', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faceinfo',
            old_name='goods_front_image_small',
            new_name='picture',
        ),
    ]
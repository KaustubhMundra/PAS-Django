# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20160624_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(max_length=120, null=True),
        ),
    ]

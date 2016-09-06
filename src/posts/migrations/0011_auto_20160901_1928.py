# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 19:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20160901_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='experience_required',
        ),
        migrations.RemoveField(
            model_name='post',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='width_field',
        ),
        migrations.AddField(
            model_name='post',
            name='field1',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 25, 13, 588987, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='field10',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 25, 33, 833901, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='field2',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 25, 41, 551824, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='field3',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 25, 49, 193064, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='field4',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 26, 5, 728697, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='field5',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 26, 21, 822903, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='field6',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 26, 30, 304903, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='field7',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 27, 50, 784859, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='field8',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 27, 56, 459707, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='field9',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 28, 5, 368690, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='salary',
            field=models.TextField(default=datetime.datetime(2016, 9, 1, 19, 28, 15, 12567, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
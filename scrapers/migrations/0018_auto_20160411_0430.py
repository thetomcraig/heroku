# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 04:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0017_auto_20160408_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterhashtag',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2016, 4, 11, 4, 29, 40, 248485, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='scrapers.TwitterPerson'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitterlink',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2016, 4, 11, 4, 29, 47, 836297, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='scrapers.TwitterPerson'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twittermention',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2016, 4, 11, 4, 30, 3, 145618, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='scrapers.TwitterPerson'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitterpost',
            name='hex_key',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]

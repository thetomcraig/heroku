# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0025_twitterpostcache'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterpostcache',
            name='beginning',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0023_twitterpost_happiness'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterpostmarkov',
            name='randomness',
            field=models.FloatField(default=0.0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 22:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0029_auto_20160510_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitterperson',
            name='name',
        ),
    ]

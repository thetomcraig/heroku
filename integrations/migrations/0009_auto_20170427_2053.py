# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-27 20:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0008_auto_20170427_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twitterconversationpost',
            old_name='content',
            new_name='post',
        ),
    ]

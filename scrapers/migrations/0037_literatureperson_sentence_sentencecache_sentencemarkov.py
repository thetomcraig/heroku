# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 05:06
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('scrapers', '0036_auto_20160529_0444'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiteraturePerson',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('real_name', models.CharField(default=b'PLACEHOLDER', max_length=1000, null=True)),
                ('avatar', models.CharField(default=b'PLACEHOLDER', max_length=1000, null=True)),
                ('happiness', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default=b'PLACEHOLDER', max_length=1000, null=True)),
                ('happiness', models.FloatField(default=0)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scrapers.LiteraturePerson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SentenceCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word1', models.CharField(default=b'PLACEHOLDER', max_length=1000, null=True)),
                ('word2', models.CharField(default=b'PLACEHOLDER', max_length=1000, null=True)),
                ('final_word', models.CharField(default=b'PLACEHOLDER', max_length=1000, null=True)),
                ('beginning', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scrapers.LiteraturePerson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SentenceMarkov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default=b'PLACEHOLDER', max_length=1000, null=True)),
                ('randomness', models.FloatField(default=0.0)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scrapers.LiteraturePerson')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

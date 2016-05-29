# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 19:39
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('scrapers', '0032_auto_20160521_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('real_name', models.CharField(default=b'PLACEHOLDER', max_length=1000, null=True)),
                ('avatar', models.CharField(default=b'PLACEHOLDER', max_length=1000, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='twitterperson',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='twitterperson',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='twitterperson',
            name='real_name',
        ),
        migrations.RemoveField(
            model_name='twitterperson',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='twitterpost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='twitterpostmarkov',
            name='author',
        ),
        migrations.AddField(
            model_name='markovchain',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scrapers.Person'),
        ),
        migrations.AddField(
            model_name='sentence',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scrapers.Person'),
        ),
        migrations.AddField(
            model_name='twitterperson',
            name='person_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scrapers.Person'),
            preserve_default=False,
        ),
    ]

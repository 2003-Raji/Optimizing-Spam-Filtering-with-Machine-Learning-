# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-30 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spam_category', models.CharField(max_length=250)),
                ('spam_list', models.CharField(max_length=250)),
            ],
        ),
    ]

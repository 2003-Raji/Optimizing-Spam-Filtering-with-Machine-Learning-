# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-04 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_sendmailmodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=300)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.RegisterModel')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-30 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='NewPost', max_length=250),
        ),
    ]

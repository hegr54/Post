# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-06 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180206_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='auther_email',
            field=models.EmailField(blank=True, max_length=240, null=True),
        ),
    ]

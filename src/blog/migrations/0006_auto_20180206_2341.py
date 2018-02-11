# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-06 23:41
from __future__ import unicode_literals

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_auther_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='auther_email',
            field=models.EmailField(blank=True, max_length=240, null=True, validators=[blog.validators.validate_author_email]),
        ),
    ]
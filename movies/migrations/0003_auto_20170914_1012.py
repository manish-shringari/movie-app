# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20170911_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(editable=False, max_length=140),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-13 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20190513_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.URLField(blank=True, verbose_name='网站'),
        ),
    ]
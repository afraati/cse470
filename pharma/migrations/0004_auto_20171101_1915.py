# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pharma', '0003_auto_20171101_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phn_no',
            field=models.BigIntegerField(),
        ),
    ]
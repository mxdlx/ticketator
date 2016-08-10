# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-10 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160808_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='color',
            field=models.CharField(blank=True, default='008ac6', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatar/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-25 06:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataModel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_user',
            old_name='name',
            new_name='username',
        ),
    ]

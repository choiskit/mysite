# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-04 18:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='quesstion',
            new_name='question',
        ),
    ]
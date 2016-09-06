# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_with_default', models.DateTimeField(default=django.utils.timezone.now)),
                ('dt_without_default', models.DateTimeField()),
            ],
        ),
    ]

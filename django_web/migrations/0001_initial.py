# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-10 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('title', models.CharField(max_length=16)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=32)),
                ('moto', models.CharField(max_length=32)),
                ('work_experice', models.CharField(max_length=32)),
                ('hobby', models.CharField(max_length=32)),
                ('study_direction', models.CharField(max_length=32)),
                ('introduction', models.TextField()),
                ('achievement', models.TextField()),
            ],
        ),
    ]

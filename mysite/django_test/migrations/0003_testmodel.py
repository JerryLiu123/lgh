# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0002_delete_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testKey', models.CharField(max_length=20)),
                ('testValue', models.CharField(max_length=20)),
                ('testTitle', models.CharField(max_length=20)),
            ],
        ),
    ]

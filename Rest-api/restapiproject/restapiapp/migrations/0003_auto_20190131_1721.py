# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapiapp', '0002_auto_20190131_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='loginmodel',
            name='username',
            field=models.CharField(primary_key=True, max_length=30, serialize=False),
        ),
    ]

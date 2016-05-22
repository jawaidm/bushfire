# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0009_auto_20160521_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='time',
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]

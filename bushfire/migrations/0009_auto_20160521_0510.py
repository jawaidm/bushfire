# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0008_auto_20160521_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]

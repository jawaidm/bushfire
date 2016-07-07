# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0016_auto_20160705_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bushfire',
            name='weather',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0012_auto_20160701_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bushfire',
            name='other_cause',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Other', blank=True),
            preserve_default=True,
        ),
    ]

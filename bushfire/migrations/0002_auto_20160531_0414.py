# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='other_cause',
            field=models.CharField(max_length=25, null=True, verbose_name=b'Other', blank=True),
            preserve_default=True,
        ),
    ]

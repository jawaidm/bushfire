# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0007_auto_20160521_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='place',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0010_auto_20160630_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='other_agency',
            field=models.CharField(default=1, max_length=50, verbose_name=b'Other Agency'),
            preserve_default=False,
        ),
    ]

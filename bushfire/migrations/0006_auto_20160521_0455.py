# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0005_auto_20160521_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='place',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]

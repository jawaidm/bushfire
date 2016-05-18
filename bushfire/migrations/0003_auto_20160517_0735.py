# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0002_auto_20160517_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bushfire',
            name='district',
            field=models.ForeignKey(to='bushfire.District'),
            preserve_default=True,
        ),
    ]

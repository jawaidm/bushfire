# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0011_bushfire_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='location',
            field=models.ForeignKey(default=1, to='bushfire.Location'),
            preserve_default=False,
        ),
    ]

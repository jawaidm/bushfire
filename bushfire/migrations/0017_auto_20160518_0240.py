# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0016_auto_20160517_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfire',
            name='authorised_by',
        ),
        migrations.AddField(
            model_name='authorisation',
            name='bushfire',
            field=models.ForeignKey(related_name='authorisation', default=1, to='bushfire.Bushfire'),
            preserve_default=False,
        ),
    ]

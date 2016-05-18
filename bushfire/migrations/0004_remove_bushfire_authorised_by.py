# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0003_auto_20160517_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfire',
            name='authorised_by',
        ),
    ]

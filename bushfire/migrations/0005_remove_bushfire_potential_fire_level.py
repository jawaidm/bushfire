# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0004_remove_bushfire_authorised_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfire',
            name='potential_fire_level',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0009_bushfiretest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfiretest',
            name='created',
        ),
        migrations.RemoveField(
            model_name='bushfiretest',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='bushfiretest',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='bushfiretest',
            name='modifier',
        ),
    ]

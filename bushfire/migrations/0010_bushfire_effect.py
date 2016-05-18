# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0009_bushfire_first_attack'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='effect',
            field=models.ForeignKey(default=1, to='bushfire.Effect'),
            preserve_default=False,
        ),
    ]

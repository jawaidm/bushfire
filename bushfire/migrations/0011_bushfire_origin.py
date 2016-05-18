# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0010_bushfire_effect'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='origin',
            field=models.ForeignKey(default=1, to='bushfire.Origin'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0012_bushfire_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='comments',
            field=models.ForeignKey(default=1, to='bushfire.Comment'),
            preserve_default=False,
        ),
    ]

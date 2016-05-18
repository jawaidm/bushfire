# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0007_bushfire_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfire',
            name='comments',
        ),
        migrations.AddField(
            model_name='bushfire',
            name='details',
            field=models.ForeignKey(default=1, to='bushfire.Detail'),
            preserve_default=False,
        ),
    ]

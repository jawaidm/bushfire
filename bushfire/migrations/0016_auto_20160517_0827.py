# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0015_auto_20160517_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfire',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='bushfire',
            field=models.ForeignKey(related_name='comments', default=1, to='bushfire.Bushfire'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0003_remove_authorisation_bushfire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='bushfire',
        ),
        migrations.AddField(
            model_name='detail',
            name='final_bushfire',
            field=models.OneToOneField(related_name='final_detail', default=1, to='bushfire.FinalBushfire'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='initial_bushfire',
            field=models.OneToOneField(related_name='initial_detail', default=1, to='bushfire.InitialBushfire'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='initialcomment',
            name='bushfire',
            field=models.OneToOneField(related_name='initial_comments', to='bushfire.InitialBushfire'),
            preserve_default=True,
        ),
    ]

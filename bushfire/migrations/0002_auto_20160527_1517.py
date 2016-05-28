# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='origin',
            name='bushfire',
        ),
        migrations.AddField(
            model_name='authorisation',
            name='final_bushfire',
            field=models.OneToOneField(related_name='final_authorisation', default=1, to='bushfire.FinalBushfire'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authorisation',
            name='initial_bushfire',
            field=models.OneToOneField(related_name='initial_authorisation', default=1, to='bushfire.InitialBushfire'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='final_bushfire',
            field=models.OneToOneField(related_name='final_location', default=1, to='bushfire.FinalBushfire'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='initial_bushfire',
            field=models.OneToOneField(related_name='initial_location', default=1, to='bushfire.InitialBushfire'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='origin',
            name='final_bushfire',
            field=models.OneToOneField(related_name='final_origin', default=1, to='bushfire.FinalBushfire'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='origin',
            name='initial_bushfire',
            field=models.OneToOneField(related_name='initial_origin', default=1, to='bushfire.InitialBushfire'),
            preserve_default=False,
        ),
    ]

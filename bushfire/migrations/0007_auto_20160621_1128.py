# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0006_auto_20160621_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='final_control',
            field=models.ForeignKey(related_name='final_control', verbose_name=b'Final Controlling Agency', blank=True, to='bushfire.Agency', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='first_attack',
            field=models.ForeignKey(related_name='first_attack', default=1, verbose_name=b'First Attack Agency', to='bushfire.Agency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='hazard_mgt',
            field=models.ForeignKey(related_name='hazard_mgt', verbose_name=b'Hazard Management Agency', blank=True, to='bushfire.Agency', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='initial_control',
            field=models.ForeignKey(related_name='initial_control', verbose_name=b'Initial Controlling Agency', blank=True, to='bushfire.Agency', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firstattackagency',
            name='bushfire',
            field=models.OneToOneField(related_name='first_attacki_bushfire', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firstattackagency',
            name='final_control',
            field=models.ForeignKey(related_name='final_control_agency', verbose_name=b'Final Controlling Agency', blank=True, to='bushfire.Agency', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firstattackagency',
            name='first_attack',
            field=models.ForeignKey(related_name='first_attack_agency', verbose_name=b'First Attack Agency', to='bushfire.Agency'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firstattackagency',
            name='hazard_mgt',
            field=models.ForeignKey(related_name='hazard_mgt_agency', verbose_name=b'Hazard Management Agency', blank=True, to='bushfire.Agency', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firstattackagency',
            name='initial_control',
            field=models.ForeignKey(related_name='initial_control_agency', verbose_name=b'Initial Controlling Agency', blank=True, to='bushfire.Agency', null=True),
            preserve_default=True,
        ),
    ]

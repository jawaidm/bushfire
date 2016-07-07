# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import smart_selects.db_fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bushfire', '0013_auto_20160701_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='BushfireTest2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Fire Name')),
                ('incident_no', models.CharField(max_length=10, verbose_name=b'Fire Incident No.')),
                ('season', models.CharField(max_length=9)),
                ('dfes_incident_no', models.CharField(max_length=10, verbose_name=b'DFES Incident No.')),
                ('job_code', models.CharField(max_length=10, null=True, verbose_name=b'Job Code', blank=True)),
                ('potential_fire_level', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3)])),
                ('init_authorised_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name=b'Authorised Date', blank=True)),
                ('district', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'region', to='bushfire.District', chained_field=b'region', auto_choose=True)),
                ('init_authorised_by', models.ForeignKey(verbose_name=b'Authorised By', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('region', models.ForeignKey(to='bushfire.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

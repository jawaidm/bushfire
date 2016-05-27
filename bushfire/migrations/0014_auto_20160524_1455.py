# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bushfire', '0013_auto_20160521_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InitialActivityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'Activity Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InitialComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('fuel', models.CharField(max_length=50)),
                ('ros', models.CharField(max_length=50, verbose_name=b'Rate of Spread')),
                ('flame_height', models.DecimalField(max_digits=12, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('assistance_required', models.CharField(max_length=50)),
                ('fire_contained', models.BooleanField(default=False)),
                ('containment_time', models.CharField(max_length=50, verbose_name=b'ET to Contain')),
                ('ops_point', models.CharField(max_length=50, verbose_name=b'OPS Point (grid ref)')),
                ('communications', models.CharField(max_length=50)),
                ('weather', models.CharField(max_length=50)),
                ('bushfire', models.OneToOneField(related_name='comments', to='bushfire.Bushfire')),
                ('creator', models.ForeignKey(related_name='bushfire_initialcomment_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('field_officer', models.ForeignKey(verbose_name=b'Field Officer', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(related_name='bushfire_initialcomment_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='finalcomment',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='finalcomment',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='finalcomment',
            name='modifier',
        ),
        migrations.DeleteModel(
            name='FinalComment',
        ),
        migrations.AddField(
            model_name='initialactivity',
            name='activity',
            field=models.ForeignKey(to='bushfire.InitialActivityType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='initialactivity',
            name='bushfire',
            field=models.ForeignKey(related_name='initial_activities', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='initialactivity',
            unique_together=set([('bushfire', 'activity')]),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='assistance_required',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='communications',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='containment_time',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='field_officer',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='fire_contained',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='flame_height',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='fuel',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='ops_point',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='ros',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='weather',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='bushfire',
            field=models.ForeignKey(related_name='final_comments', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityType',
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
            name='AerialForces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Agency Name', choices=[(1, b'Fixed Wing'), (2, b'Helicopter')])),
                ('observer', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('transporter', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ignition', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('water_bomber', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Agency Name')),
                ('code', models.CharField(max_length=10, verbose_name=b'Agency Short Code')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AreaBurnt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.DecimalField(verbose_name=b'Area (ha)', max_digits=12, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('origin', models.BooleanField(default=False, verbose_name=b'Point of Origin')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttendingOrganisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('other', models.CharField(max_length=25, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bushfire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Fire Name')),
                ('incident_no', models.CharField(max_length=10, verbose_name=b'Incident No.')),
                ('season', models.CharField(max_length=9)),
                ('dfes_incident_no', models.CharField(max_length=10, verbose_name=b'DFES Incident No.')),
                ('job_code', models.CharField(max_length=10, null=True, verbose_name=b'Job Code', blank=True)),
                ('potential_fire_level', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3)])),
                ('authorised_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name=b'Authorised Date', blank=True)),
                ('distance', models.DecimalField(verbose_name=b'Distance (km)', max_digits=6, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('place', models.CharField(max_length=25)),
                ('lot_no', models.CharField(max_length=10, verbose_name=b'Lot Number')),
                ('street', models.CharField(max_length=25)),
                ('town', models.CharField(max_length=25)),
                ('authorised_by', models.ForeignKey(verbose_name=b'Authorised By', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('creator', models.ForeignKey(related_name='bushfire_bushfire_created', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('bushfire', models.ForeignKey(related_name='final_comments', to='bushfire.Bushfire')),
                ('creator', models.ForeignKey(related_name='bushfire_comment_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(related_name='bushfire_comment_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.DecimalField(verbose_name=b'Area (ha)', max_digits=12, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('other_agency', models.CharField(max_length=25, null=True, verbose_name=b'Other', blank=True)),
                ('dec', models.BooleanField(default=False, verbose_name=b'DEC')),
                ('lga_bfb', models.BooleanField(default=False, verbose_name=b'LGA BFB')),
                ('fesa', models.BooleanField(default=False, verbose_name=b'FESA')),
                ('ses', models.BooleanField(default=False, verbose_name=b'SES')),
                ('police', models.BooleanField(default=False, verbose_name=b'POLICE')),
                ('other_force', models.CharField(max_length=25, null=True, verbose_name=b'Other', blank=True)),
                ('known_possible', models.PositiveSmallIntegerField(verbose_name=b'Known/Possible', choices=[(1, b'Known'), (2, b'Possible')])),
                ('other_cause', models.CharField(max_length=25, null=True, verbose_name=b'Other', blank=True)),
                ('investigation_req', models.BooleanField(default=False, verbose_name=b"Invest'n Required")),
                ('bushfire', models.OneToOneField(related_name='detail', to='bushfire.Bushfire')),
                ('cause', models.ForeignKey(to='bushfire.Cause')),
                ('first_attack', models.ForeignKey(to='bushfire.Agency')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('code', models.CharField(max_length=3)),
                ('archive_date', models.DateField(help_text=b'Archive this District (prevent from creating new ePFPs)', null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fire_stopped', models.PositiveSmallIntegerField(null=True, verbose_name=b'Fuel Age - Fire Stopped (Yr)', blank=True)),
                ('last_burnt', models.PositiveSmallIntegerField(null=True, verbose_name=b'Fuel Age - Area Last Burnt (Yr)', blank=True)),
                ('arrival_area', models.DecimalField(verbose_name=b'Fire Area at Arrival (ha)', max_digits=12, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('fire_level', models.PositiveSmallIntegerField(verbose_name=b'Final Fire Level', choices=[(1, 1), (2, 2), (3, 3)])),
                ('bushfire', models.OneToOneField(related_name='effects', to='bushfire.Bushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FireBehaviour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'Name/Description', blank=True)),
                ('fuel_weight', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('fdi', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ros', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('bushfire', models.ForeignKey(related_name='fire_behaviour', to='bushfire.Bushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FirstAttackAgency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bushfire', models.OneToOneField(related_name='first_attack', to='bushfire.Bushfire')),
                ('final_control', models.ForeignKey(related_name='final_control', verbose_name=b'Final Controlling Agency', blank=True, to='bushfire.Agency', null=True)),
                ('first_attack', models.ForeignKey(related_name='first_attack', verbose_name=b'First Attack Agency', to='bushfire.Agency')),
                ('hazard_mgt', models.ForeignKey(related_name='hazard_mgt', verbose_name=b'Hazard Management Agency', blank=True, to='bushfire.Agency', null=True)),
                ('initial_control', models.ForeignKey(related_name='initial_control', verbose_name=b'Initial Controlling Agency', blank=True, to='bushfire.Agency', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FrbEffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroundForces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Agency Name', choices=[(1, b'Initial DEC Dispatch'), (2, b'DEC Peak'), (3, b'Other Agencies Peak')])),
                ('persons', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('pumpers', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('plant', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('bushfire', models.ForeignKey(related_name='ground_forces', to='bushfire.Bushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Initial',
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
                ('communications', models.CharField(max_length=50, verbose_name=b'Communication')),
                ('weather', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('authorised_by', models.ForeignKey(verbose_name=b'Authorising Officer', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('bushfire', models.OneToOneField(related_name='initial_report', to='bushfire.Bushfire')),
                ('creator', models.ForeignKey(related_name='bushfire_initial_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('field_officer', models.ForeignKey(related_name='field_officer', verbose_name=b'Field Officer', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(related_name='bushfire_initial_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvestigationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Investigation Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Legal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protection', models.PositiveSmallIntegerField(verbose_name=b'Community Protection (%)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('cost', models.DecimalField(verbose_name=b'Est. Cost of Damages ($)', max_digits=12, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('restricted_period', models.BooleanField(default=False)),
                ('prohibited_period', models.BooleanField(default=False)),
                ('bushfire', models.ForeignKey(related_name='legal', to='bushfire.Bushfire')),
                ('inv_undertaken', models.ForeignKey(verbose_name=b'Investigation Undertaken', to='bushfire.InvestigationType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LegalResultType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Legal Result Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.DecimalField(verbose_name=b'Distance (km)', max_digits=6, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('place', models.CharField(max_length=25)),
                ('lot_no', models.CharField(max_length=10, verbose_name=b'Lot Number')),
                ('street', models.CharField(max_length=25)),
                ('town', models.CharField(max_length=25)),
                ('bushfire', models.OneToOneField(related_name='location', to='bushfire.Bushfire')),
                ('direction', models.ForeignKey(verbose_name=b'Direction', to='bushfire.Direction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.DecimalField(verbose_name=b'Distance (km)', max_digits=6, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('place', models.CharField(max_length=25)),
                ('lot_no', models.CharField(max_length=10, verbose_name=b'Lot Number')),
                ('street', models.CharField(max_length=25)),
                ('town', models.CharField(max_length=25)),
                ('direction', models.ForeignKey(verbose_name=b'Direction', to='bushfire.Direction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Organisation')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coord_type', models.PositiveSmallIntegerField(verbose_name=b'Coordinate Type', choices=[(1, b'MGA'), (2, b'Lat/Long'), (3, b'FD Grid')])),
                ('fire_not_found', models.BooleanField(default=False)),
                ('lat_decimal', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Decimal)')),
                ('lat_degrees', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Degrees)')),
                ('lat_minutes', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Minutes)')),
                ('lon_decimal', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Decimal)')),
                ('lon_degrees', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Degrees)')),
                ('lon_minutes', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Minutes)')),
                ('mga_zone', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Zone')),
                ('mga_easting', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Easting')),
                ('mga_northing', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Northing')),
                ('fd_letter', models.CharField(max_length=2, null=True, verbose_name=b'FD Letter', blank=True)),
                ('fd_number', models.PositiveSmallIntegerField(null=True, verbose_name=b'FD Number', blank=True)),
                ('fd_tenths', models.CharField(max_length=2, null=True, verbose_name=b'FD Tenths', blank=True)),
                ('bushfire', models.OneToOneField(related_name='origin', to='bushfire.Bushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('burn_id', models.CharField(max_length=7)),
            ],
            options={
                'ordering': ['burn_id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriorityRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrivateDamage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('bushfire', models.ForeignKey(related_name='private_damages', to='bushfire.Bushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrivateDamageType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'Private Damage Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicDamage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.DecimalField(verbose_name=b'Area (ha)', max_digits=12, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('bushfire', models.ForeignKey(related_name='public_damages', to='bushfire.Bushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicDamageType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Public Damage Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arson_squad_notified', models.BooleanField(default=False, verbose_name=b'Arson Squad Notified')),
                ('offence_no', models.CharField(max_length=10, verbose_name=b'Offence No.')),
                ('bushfire', models.OneToOneField(related_name='reporting', to='bushfire.Bushfire')),
                ('cause', models.ForeignKey(to='bushfire.Cause')),
                ('prescription', models.ForeignKey(verbose_name=b'Prescription Burn ID', blank=True, to='bushfire.Prescription', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bushfire', models.ForeignKey(related_name='responses', to='bushfire.Bushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResponseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Agency Name')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tenure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WaterBombEffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='response',
            name='response',
            field=models.ForeignKey(to='bushfire.ResponseType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='response',
            unique_together=set([('bushfire', 'response')]),
        ),
        migrations.AddField(
            model_name='reporter',
            name='source',
            field=models.ForeignKey(verbose_name=b'Reported By', blank=True, to='bushfire.Source', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicdamage',
            name='damage_type',
            field=models.ForeignKey(to='bushfire.PublicDamageType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicdamage',
            name='fuel_type',
            field=models.ForeignKey(to='bushfire.FuelType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='publicdamage',
            unique_together=set([('bushfire', 'damage_type', 'fuel_type')]),
        ),
        migrations.AddField(
            model_name='privatedamage',
            name='damage_type',
            field=models.ForeignKey(to='bushfire.PrivateDamageType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='privatedamage',
            unique_together=set([('bushfire', 'damage_type')]),
        ),
        migrations.AddField(
            model_name='legal',
            name='legal_result',
            field=models.ForeignKey(to='bushfire.LegalResultType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='groundforces',
            unique_together=set([('bushfire', 'name')]),
        ),
        migrations.AddField(
            model_name='firebehaviour',
            name='fuel_type',
            field=models.ForeignKey(related_name='fuel_types_fire', blank=True, to='bushfire.FuelType', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='firebehaviour',
            unique_together=set([('bushfire', 'name')]),
        ),
        migrations.AddField(
            model_name='effect',
            name='frb_effect',
            field=models.ForeignKey(verbose_name=b'Presence/Effect of FRB', blank=True, to='bushfire.FrbEffect', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='effect',
            name='rating',
            field=models.ForeignKey(verbose_name=b'Area Priority Rating', to='bushfire.PriorityRating'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='effect',
            name='waterbomb_effect',
            field=models.ForeignKey(verbose_name=b'Presence/Effect of WaterBomb', blank=True, to='bushfire.WaterBombEffect', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(to='bushfire.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='fuel_type',
            field=models.ForeignKey(to='bushfire.FuelType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='tenure',
            field=models.ForeignKey(to='bushfire.Tenure'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='direction',
            field=models.ForeignKey(verbose_name=b'Direction', to='bushfire.Direction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='district',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'region', to='bushfire.District', chained_field=b'region', auto_choose=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='modifier',
            field=models.ForeignKey(related_name='bushfire_bushfire_modified', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='region',
            field=models.ForeignKey(to='bushfire.Region'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='bushfire',
            unique_together=set([('district', 'incident_no', 'season')]),
        ),
        migrations.AddField(
            model_name='attendingorganisation',
            name='bushfire',
            field=models.ForeignKey(related_name='attending_organisations', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendingorganisation',
            name='name',
            field=models.ForeignKey(blank=True, to='bushfire.Organisation', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='attendingorganisation',
            unique_together=set([('bushfire', 'name')]),
        ),
        migrations.AddField(
            model_name='areaburnt',
            name='bushfire',
            field=models.ForeignKey(related_name='areas_burnt', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaburnt',
            name='fuel_type',
            field=models.ForeignKey(related_name='fuel_types', to='bushfire.FuelType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaburnt',
            name='tenure',
            field=models.ForeignKey(related_name='tenures', to='bushfire.Tenure'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='areaburnt',
            unique_together=set([('bushfire', 'tenure', 'fuel_type')]),
        ),
        migrations.AddField(
            model_name='aerialforces',
            name='bushfire',
            field=models.ForeignKey(related_name='aerial_forces', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='aerialforces',
            unique_together=set([('bushfire', 'name')]),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity',
            field=models.ForeignKey(to='bushfire.ActivityType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='bushfire',
            field=models.ForeignKey(related_name='activities', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='activity',
            unique_together=set([('bushfire', 'activity')]),
        ),
    ]

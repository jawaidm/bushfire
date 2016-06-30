from django import forms
from bushfire.models import (Bushfire, Activity, Response, AreaBurnt, GroundForces, AerialForces,
        AttendingOrganisation, FireBehaviour, Legal, PrivateDamage, PublicDamage, Comment,
        Region, District
    )
from datetime import datetime, timedelta
from django.conf import settings
from django.forms import ValidationError
from django.forms.models import inlineformset_factory, modelformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from crispy_forms.bootstrap import TabHolder, Tab


class ActivityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
##        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Div(
                Div('activity',css_class='col-sm-4',),
                Div('date',css_class='col-sm-2',),
                css_class='row activity-formset',
            ),
        )

    class Meta:
        model = Activity
        # fields = ('activity', 'date',)
        exclude = ()


class BushfireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        if kwargs.has_key('user'):
            user = kwargs.pop('user')
        super(BushfireForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        #self.helper.form_method = 'post'
#        self.helper.form_class = 'form-horizontal'
#        self.helper.label_class = 'col-sm-2'
#        self.helper.field_class = 'col-sm-8'

        self.helper.layout = Layout(
            Div(
                Div('region',css_class='col-sm-2',),
                Div('district',css_class='col-sm-2',),
                Div('incident_no',css_class='col-sm-2',),
                Div('season',css_class='col-sm-2',),
                Div('job_code',css_class='col-sm-2',),
                css_class='row',
            ),
            Div(
                Div('name',css_class='col-sm-2',),
                Div('dfes_incident_no',css_class='col-sm-2',),
                Div('potential_fire_level',css_class='col-sm-2',),
                Div('authorised_by',css_class='col-sm-2',),
                Div('authorised_date',css_class='col-sm-2',),
                css_class='row',
            ),
            HTML('<hr>'),
            Div(
                Div('source',css_class='col-sm-3',),
                Div('cause',css_class='col-sm-3',),
                Div('arson_squad_notified',css_class='col-sm-2',),
                Div('prescription',css_class='col-sm-2',),
                Div('offence_no',css_class='col-sm-2',),
                css_class='row',
            ),
            HTML('<hr>'),


            TabHolder(
#                self.add_origin(),
#                self.add_location(),
                self.add_activities(),
                self.add_comments(),
#                Tab(
#                    'Location',
#                    Div(
#                        Div('distance',css_class='col-sm-2',),
#                        Div('direction',css_class='col-sm-2',),
#                        Div('place',css_class='col-sm-4',),
#                        Div('lot_no',css_class='col-sm-2',),
#                        css_class='row',
#                    ),
#                    Div(
#                        Div('street',css_class='col-sm-4',),
#                        Div('town',css_class='col-sm-2',),
#                        css_class='row',
#                    ),
#                ),
#            ),

#            ButtonHolder(
#                Submit('submit', 'Submit', css_class='button white')
            )

        )

    def add_origin(self):
        return Tab(
            'Point of Origin',
            Div(
                Div('coord_type',css_class='col-sm-2',),
                Div('fire_not_found',css_class='col-sm-2',),
                css_class='row',
            ),
            HTML('<hr>'),
            Div(
                Div(
                    Div('lat_decimal',css_class='col-sm-2',),
                    Div('lat_degrees',css_class='col-sm-2',),
                    Div('lat_minutes',css_class='col-sm-2',),
                    css_class='row',
                ),
                Div(
                    Div('lon_decimal',css_class='col-sm-2',),
                    Div('lon_degrees',css_class='col-sm-2',),
                    Div('lon_minutes',css_class='col-sm-2',),
                    css_class='row',
                ),
            ),
            HTML('<hr>'),
            Div(
                Div('mga_zone',css_class='col-sm-2',),
                Div('mga_easting',css_class='col-sm-2',),
                Div('mga_northing',css_class='col-sm-2',),
                css_class='row',
            ),
            HTML('<hr>'),
            Div(
                Div('fd_letter',css_class='col-sm-2',),
                Div('fd_number',css_class='col-sm-2',),
                Div('fd_tenths',css_class='col-sm-2',),
                css_class='row',
            ),
            HTML('<hr>'),

        )

    def add_location(self):
        return Tab(
            'Location',
            Div(
                Div('distance',css_class='col-sm-2',),
                Div('direction',css_class='col-sm-2',),
                Div('place',css_class='col-sm-4',),
                Div('lot_no',css_class='col-sm-2',),
                css_class='row',
            ),
            Div(
                Div('street',css_class='col-sm-4',),
                Div('town',css_class='col-sm-2',),
                css_class='row',
            ),
        )

    def add_activities(self):
        return Tab(
            'Activities',
            HTML('<p>My Activities</p>'),
            Div(
                Div('activity',css_class='col-sm-2',),
                Div('date',css_class='col-sm-2',),
            ),
        )

    def add_comments(self):
        return Tab(
            'Comment',
            HTML('<p>My Comments</p>'),
            Div(
                Div('comment',css_class='col-sm-6',),
            ),
        )

    class Meta:
        model = Bushfire
        fields = ('region', 'district', 'incident_no', 'season', 'job_code',
                  'name', 'dfes_incident_no', 'potential_fire_level', 'authorised_by', 'authorised_date',
                  'source','cause', 'arson_squad_notified', 'prescription', 'offence_no',
#                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
#                  'coord_type', 'fire_not_found', 'lat_decimal', 'lat_degrees', 'lat_minutes',
#                  'lon_decimal', 'lon_degrees', 'lon_minutes', 'mga_zone', 'mga_easting', 'mga_northing',
#                  'fd_letter', 'fd_number', 'fd_tenths',
#                  'fuel','ros', 'flame_height', 'assistance_required', 'fire_contained', 'containment_time',
#                  'ops_point', 'communications', 'weather', 'field_officer', 'init_authorised_by', 'init_authorised_date',
                 )
#        exclude = ()


class _BushfireForm(forms.ModelForm):
    class Meta:
        model = Bushfire
        fields = ('region', 'district', 'incident_no', 'season', 'job_code',
                  'name', 'dfes_incident_no', 'potential_fire_level', 'authorised_by', 'authorised_date',
                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
                  'coord_type', 'fire_not_found', 'lat_decimal', 'lat_degrees', 'lat_minutes',
                  'lon_decimal', 'lon_degrees', 'lon_minutes', 'mga_zone', 'mga_easting', 'mga_northing',
                  'fd_letter', 'fd_number', 'fd_tenths',
#                  'source','cause', 'arson_squad_notified', 'prescription', 'offence_no',
#                  'fuel','ros', 'flame_height', 'assistance_required', 'fire_contained', 'containment_time',
#                  'ops_point', 'communications', 'weather', 'field_officer', 'init_authorised_by', 'init_authorised_date',
                 )
#        exclude = ()


#ActivityFormSet             = inlineformset_factory(Bushfire, Activity, extra=1, max_num=7, can_delete=True)
ActivityFormSet             = inlineformset_factory(Bushfire, Activity, form=ActivityForm, extra=1, max_num=7, can_delete=True)
#ActivityFormSet             = modelformset_factory(Activity, form=ActivityForm, extra=1, max_num=7, can_delete=True)
ResponseFormSet             = inlineformset_factory(Bushfire, Response, extra=1, max_num=13, can_delete=True)
AreaBurntFormSet            = inlineformset_factory(Bushfire, AreaBurnt, extra=1, can_delete=True)
GroundForcesFormSet         = inlineformset_factory(Bushfire, GroundForces, extra=1, max_num=3, can_delete=True)
AerialForcesFormSet         = inlineformset_factory(Bushfire, AerialForces, extra=1, can_delete=True)
AttendingOrganisationFormSet= inlineformset_factory(Bushfire, AttendingOrganisation, extra=1, max_num=11, can_delete=True)
FireBehaviourFormSet        = inlineformset_factory(Bushfire, FireBehaviour, extra=1, can_delete=True)
LegalFormSet                = inlineformset_factory(Bushfire, Legal, extra=1, max_num=12, can_delete=True)
PrivateDamageFormSet        = inlineformset_factory(Bushfire, PrivateDamage, extra=1, max_num=12, can_delete=True)
PublicDamageFormSet         = inlineformset_factory(Bushfire, PublicDamage, extra=1, can_delete=True)
CommentFormSet              = inlineformset_factory(Bushfire, Comment, extra=1, can_delete=True)




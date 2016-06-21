from django import forms
from bushfire.models import Bushfire, Activity, Response, Region, District
from datetime import datetime, timedelta
from django.conf import settings
from django.forms import ValidationError
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from crispy_forms.bootstrap import TabHolder, Tab


class _ActivityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        super(ActivityForm, self).__init__(*args, **kwargs)

#        self.helper = FormHelper()
##        self.helper.form_method = 'post'
#
#        self.helper.layout = Layout(
#            Div(
#                Div('activity',css_class='col-sm-2',),
#                Div('date',css_class='col-sm-2',),
#                css_class='row',
#            ),
#        )

    class Meta:
        model = Activity
        fields = ('activity', 'date',)


class _BushfireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        if kwargs.has_key('user'):
            user = kwargs.pop('user')
        super(BushfireForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
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


            TabHolder(
                self.add_origin(),
                self.add_location(),
                #self.add_activities(),
                Tab(
                    'PlaceHolder',
                    #'location2',
                ),
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
            ),

#            ButtonHolder(
#                Submit('submit', 'Submit', css_class='button white')
#            )

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
            Div(
                Div('activity',css_class='col-sm-2',),
                Div('date',css_class='col-sm-2',),
            ),
        )
    class Meta:
        model = Bushfire
        #fields = ('region', 'district', 'incident_no', 'season', 'job_code',)
        fields = ('region', 'district', 'incident_no', 'season', 'job_code',
                  'name', 'dfes_incident_no', 'potential_fire_level', 'authorised_by', 'authorised_date',
                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
                  'coord_type', 'fire_not_found', 'lat_decimal', 'lat_degrees', 'lat_minutes',
                  'lon_decimal', 'lon_degrees', 'lon_minutes', 'mga_zone', 'mga_easting', 'mga_northing',
                  'fd_letter', 'fd_number', 'fd_tenths',
                 )


class BushfireForm(forms.ModelForm):
    class Meta:
        model = Bushfire
#        fields = ('region', 'district', 'incident_no', 'season', 'job_code',
#                  'name', 'dfes_incident_no', 'potential_fire_level', 'authorised_by', 'authorised_date',
#                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
#                  'coord_type', 'fire_not_found', 'lat_decimal', 'lat_degrees', 'lat_minutes',
#                  'lon_decimal', 'lon_degrees', 'lon_minutes', 'mga_zone', 'mga_easting', 'mga_northing',
#                  'fd_letter', 'fd_number', 'fd_tenths',
#                  'source','cause', 'arson_squad_notified', 'prescription', 'offence_no',
#                  'fuel','ros', 'flame_height', 'assistance_required', 'fire_contained', 'containment_time',
#                  'ops_point', 'communications', 'weather', 'field_officer', 'init_authorised_by', 'init_authorised_date',
#                 )
        exclude = ()


ActivityFormSet = inlineformset_factory(Bushfire, Activity, extra=1, max_num=7)
ResponseFormSet = inlineformset_factory(Bushfire, Response, extra=1, max_num=13, can_delete=True)




from django import forms
from bushfire.models import Bushfire, Region, District
from datetime import datetime, timedelta
from django.conf import settings
from django.forms import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from crispy_forms.bootstrap import TabHolder, Tab

class BushfireForm(forms.ModelForm):
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
                Tab(
                    'Point of Origin',
                    #'location2',
                ),
                self.add_location()
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

            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )

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

    class Meta:
        model = Bushfire
        fields = ('name', 'region', 'district', 'incident_no', 'season', 'job_code',
                  'name', 'dfes_incident_no', 'potential_fire_level',
                  'authorised_by', 'authorised_date',
                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
                 )




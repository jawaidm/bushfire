from django import forms
from bushfire.models import Bushfire, Region, District
from datetime import datetime, timedelta
from django.conf import settings
from django.forms import ValidationError


class BushfireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        if kwargs.has_key('user'):
            user = kwargs.pop('user')
        super(BushfireForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Bushfire
        #fields = ('name',)




from django import forms

from .models import Event
from .models import Organization
from .models import RepeatingEvent 
from django.contrib.auth.models import User
from django.contrib.admin import widgets 


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ('organization_name',)

class EventForm(forms.ModelForm):
	start_time = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)
	end_time = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)
	#event_type = forms.CharField(required=False)
	event_url = forms.URLField(required=False)
	location = forms.CharField(required=False)

	class Meta:
		model = Event
		fields = ('event_title', 'start_time', 'end_time', 'event_type', 'event_url', 'location',)

class RepeatingEventForm(forms.ModelForm):
	end_repeat = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime, required=False)

	class Meta:
		model = RepeatingEvent
		fields = ('frequency', 'day_of_week', 'end_repeat')

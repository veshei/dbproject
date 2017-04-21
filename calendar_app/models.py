# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django import forms

from django.contrib.auth.models import User


# Create your models here.

class Event(models.Model):
	type_choices = (
	('General meeting', 'General Meeting'), 
	('Fundraiser', 'Fundraiser'), 
	('Event', 'Event'), 
	('Other', 'Other')
)
	frequency_choices = (
	('daily', 'Daily'),
	('weekly', 'Weekly'),
	('monthly', 'Monthly'),
	('yearly', 'Yearly'),
	('none', 'None')
)
	day_choices = (
	('Sunday', 'Sunday'),
	('Monday', 'Monday'),
	('Tuesday', 'Tuesday'),
	('Wednesday', 'Wednesday'),
	('Thursday', 'Thursday'),
	('Friday', 'Friday'),
	('None', 'None')
)
	event_title = models.CharField(max_length=200, null=False)
	start_time = models.DateTimeField(null=False)
	end_time = models.DateTimeField(null=False)
	event_type = models.CharField(max_length=50, choices=type_choices)
	event_url = models.URLField(max_length=200)
	location = models.CharField(max_length=200)
	frequency = models.CharField(max_length=200, choices=frequency_choices, null=False, default='')
	day_of_week = models.CharField(max_length=200, choices=day_choices, null=False, default='')
	end_repeat = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.event_title

class Organization(models.Model):
	organization_choices = (
		('aKDPHI', 'alpha Kappa Delta Phi'),
		('ASU', 'Asian Student Union'),
		('BKD', 'Barkada'),
		('BCT', 'Beta Chi Theta'),
		('DPO', 'Delta Phi Omega'),
		('KASA', 'Korean American Student Organization'),
		('KPL', 'Kappa Phi Lambda'),
		('PDP', 'Pi Delta Psi'),
		('SASE', 'Society of Asian Scientists and Engineers'),
		('UTSAV', 'UTSAV'),
		('VSA', 'Vietnamese Student Association')
)

	organization_name = models.CharField(max_length=200, choices=organization_choices, null=False, default='')
	email = models.EmailField(max_length=254, null=False)
	website = models.URLField(max_length=200)

	def __str__(self):
		return self.organization_name

class UserOrganization(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

	def __str__(self):
		return self.user

	def __unicode__(self):
		return unicode(self.user)

class CalendarEvent(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
	contact = models.CharField(max_length=200)

	def __str__(self):
		return self.event

	def __unicode__(self):
		return unicode(self.event)

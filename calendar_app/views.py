# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import UserForm, OrganizationForm
from .forms import EventForm
from .models import Event
from .models import Organization
from .models import CalendarEvent
from .models import UserOrganization
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView


import datetime


# Create your views here.
def calendar_list(request):

    events = Event.objects.exclude(start_time__lte=datetime.date.today()).order_by('start_time')
    organizations = Organization.objects.order_by('organization_name')

    return render(request, 'calendar_app/calendar_list.html', {'events': events, 'organizations': organizations})


def org_calendar_list(request, pk):
    organizations = Organization.objects.order_by('organization_name')
    organization = get_object_or_404(Organization, pk=pk)

    events = CalendarEvent.objects.filter(organization=organization).exclude(event__start_time__lte=datetime.date.today()).order_by('event__start_time')

    return render(request, 'calendar_app/org_calendar_list.html', {'events': events, 'organizations': organizations})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    calendarevent = CalendarEvent.objects.get(event=event)
    caleventorg = calendarevent.organization
    current_user = request.user 
    if current_user.is_superuser:
    	organization = Organization.objects.all()
    elif request.user.is_active:
    	userorg = UserOrganization.objects.get(user=current_user)
    	organization = userorg.organization
    else:
    	organization = Organization.objects.all()
    return render(request, 'calendar_app/event_detail.html', {'event': event, 'caleventorg': caleventorg, 'organization': organization})


@login_required
def event_new(request):

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.event_title = form.cleaned_data['event_title']
            event.start_time = form.cleaned_data['start_time']
            event.end_time = form.cleaned_data['end_time']
            event.event_url = form.cleaned_data['event_url']
            event.location = form.cleaned_data['location']
            event.save()

            current_user = request.user
            if current_user.is_superuser:
                return redirect('calendar_list')
            else:
                userorg = UserOrganization.objects.get(user=current_user)
                organization = userorg.organization

                new_event = CalendarEvent(event=event, organization=organization, contact="None")
                new_event.save()

                return redirect('calendar_list')
    else:
        form = EventForm()


    return render(request, 'calendar_app/event_edit.html', {'form': form})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event.event_title = form.cleaned_data['event_title']
            event.start_time = form.cleaned_data['start_time']
            event.end_time = form.cleaned_data['end_time']
            event.event_url = form.cleaned_data['event_url']
            event.location = form.cleaned_data['location']
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'calendar_app/event_edit.html', {'form': form})


@login_required
def event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('calendar_list')


class UserFormView(View):
    user_form_class = UserForm
    organization_form_class = OrganizationForm
    template_name = 'registration/register.html'

    def get(self, request):
        form1 = self.user_form_class(None)
        form2 = self.organization_form_class(None)
        return render(request, self.template_name, {'user_form': form1, "organization_form": form2})

    def post(self, request):
        form1 = self.user_form_class(request.POST)
        form2 = self.organization_form_class(request.POST)

        if form1.is_valid() and form2.is_valid():

            user = form1.save(commit=False)
            org = form2.save(commit=False)

            username = form1.cleaned_data['username']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            organization_name = form2.cleaned_data['organization_name']
            user.set_password(password)
            user.save()

            orgs = Organization.objects.filter(organization_name=organization_name)
            if orgs.count() == 0:
                org.save()

            user = User.objects.get(username=username)
            organization = Organization.objects.get(organization_name=organization_name)
            userorg = UserOrganization(user=user, organization=organization)
            userorg.save()

            # returns user objects

            user = authenticate(username=username, email=email, password=password)

            if user is not None:

                if user.is_active:
                    # login(request, user)
                    return redirect('login')

        return render(request, self.template_name, {'user_form': form1, 'organization_form': form2})

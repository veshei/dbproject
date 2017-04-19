# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event
from .models import Calendar
from .models import RepeatingEvent
from .models import Organization
from .models import CalendarEvent
from .models import UserOrganization

admin.site.register(Event)
admin.site.register(Calendar)
admin.site.register(RepeatingEvent)
admin.site.register(Organization)
admin.site.register(CalendarEvent)
admin.site.register(UserOrganization)

# Register your models here.

from django.contrib import admin
from volunteerUofG.models import Opportunity, Volunteer, Charity

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(Charity)
admin.site.register(Opportunity)


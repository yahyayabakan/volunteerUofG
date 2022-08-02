from django import forms
from django.contrib.auth.models import User
from volunteerUofG.models import Charity, Opportunity, Volunteer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password','first_name', 'last_name')

class CharityForm(forms.ModelForm):
    class Meta:
        model = Charity
        fields = ('address', 'phone', 'website','description','image')

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('interested_in', 'availability','introduce_yourself','image')

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ('title','url','description', 'skills', 'creator', 'location', 'time', 'image')

            


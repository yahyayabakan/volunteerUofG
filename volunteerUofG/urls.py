from django.urls import path

from . import views

app_name = 'volunteerUofG'

urlpatterns = [
    path('', views.index, name='index'),    
    path('login/', views.user_login, name='login'),   
    path('logout/', views.user_logout, name='logout'),
    path('faq/', views.faq, name='faq'),   
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('becomeAVolunteer/', views.becomeAVolunteer, name='becomeAVolunteer'),
    path('activeVolunteers/', views.activeVolunteers, name='activeVolunteers'),
    path('findAVolunteer/', views.findAVolunteer, name='findAVolunteer'),
    path('activeOpportunities/', views.activeOpportunities, name='activeOpportunities'),
    path('createAnOpportunity/', views.createAnOpportunity, name='createAnOpportunity'),
]
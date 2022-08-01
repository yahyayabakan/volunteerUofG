import imp
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

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
    path('myOpportunities/', views.myOpportunities, name='myOpportunities'),
    path('updateOpportunity/<str:pk>/', views.updateOpportunity, name='updateOpportunity'),
    path('deleteOpportunity/<str:pk>/', views.deleteOpportunity, name='deleteOpportunity'),
    path('myAccount/<str:pk>/', views.myAccount, name='myAccount'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
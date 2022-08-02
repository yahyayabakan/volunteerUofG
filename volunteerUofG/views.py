

from django.http import HttpResponse
from django.shortcuts import render
from volunteerUofG.forms import OpportunityForm, UserForm, CharityForm, VolunteerForm
from volunteerUofG.models import Opportunity, Volunteer, Charity, User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required





def index(request):
    opportunityList = Opportunity.objects.all()
    activeOpportunitiesSize = len(opportunityList)

    volunteerList = Volunteer.objects.all()
    activeVolunteerSize = len(volunteerList)
    context = {
        "activeOpportunitiesSize" : activeOpportunitiesSize,
        "activeVolunteersSize" : activeVolunteerSize
    }
    return render(request, "volunteerUofG/index.html", context) 

def faq(request):
    return render(request, "volunteerUofG/faq.html")   

def aboutUs(request):
    return render(request, "volunteerUofG/aboutUs.html")     

def activeVolunteers(request):
    context = {
        "volunteers" : Volunteer.objects.all()
    }
    return render(request, "volunteerUofG/activeVolunteers.html", context)

def activeOpportunities(request):
    context = {
        "opportunities" : Opportunity.objects.all()
    }
    return render(request, "volunteerUofG/activeOpportunities.html", context)      



def becomeAVolunteer(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        volunteer_form = VolunteerForm(request.POST, request.FILES)  

        if user_form.is_valid() and volunteer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            volunteer = volunteer_form.save(commit=False)
            volunteer.user = user
            volunteer.save()
            
           
            registered = True
        else:
            print(user_form.errors, volunteer_form.errors)
    else:
        user_form = UserForm()
        volunteer_form = VolunteerForm()
    
    return render(request, 'volunteerUofG/becomeAVolunteer.html', context={'user_form' : user_form, 'volunteer_form' : volunteer_form, 'registered' : registered})

def findAVolunteer(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        charity_form = CharityForm(request.POST, request.FILES)  

        if user_form.is_valid() and charity_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            charity = charity_form.save(commit=False)
            charity.user = user
            charity.save()
            
           
            registered = True
        else:
            print(user_form.errors, charity_form.errors)
    else:
        user_form = UserForm()
        charity_form = CharityForm()
    
    return render(request, 'volunteerUofG/findAVolunteer.html', context={'user_form' : user_form, 'charity_form' : charity_form, 'registered' : registered})

def createAnOpportunity(request):
    registered = False

    if request.method == 'POST':
        
        opportunity_form = OpportunityForm(request.POST, request.FILES)  

        if opportunity_form.is_valid():          

            opportunity = opportunity_form.save(commit=False)            
            opportunity.save()   
            registered = True        
           
            
        else:
            print(opportunity_form.errors)
    else:
       
        opportunity_form = OpportunityForm()
    
    return render(request, 'volunteerUofG/createAnOpportunity.html', context={ 'opportunity_form' : opportunity_form, 'registered' : registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('volunteerUofG:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    
    else:
        return render(request, 'volunteerUofG/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('volunteerUofG:index'))


@login_required
def myOpportunities(request):
    allOpportunities = Opportunity.objects.all()
    
    
    def isMyOpportunity(opportunity):
        if opportunity.creator.user == request.user:
            return True
        else :
            return False
    context = {
        "myOpportunities" : filter(isMyOpportunity, allOpportunities)
    }
    return render(request, "volunteerUofG/myOpportunities.html", context) 


"""def updateOpportunity(request, pk):
    registered = False

    if request.method == 'POST':

       
        
        opportunity_form = OpportunityForm(request.POST)  

        if opportunity_form.is_valid():          

            opportunity = opportunity_form.save(commit=False)            
            opportunity.save()   
            registered = True        
           
            
        else:
            print(opportunity_form.errors)
    else:
       
        opportunity_form = OpportunityForm()
    
    return render(request, 'volunteerUofG/updateOpportunity.html', context={ 'opportunity_form' : opportunity_form, 'registered' : registered})"""

def updateOpportunity(request, pk):
    opportunity = Opportunity.objects.get(id = pk)

    opportunity_form = OpportunityForm( instance = opportunity) 
    

    if request.method == 'POST':
        opportunity_form = OpportunityForm(request.POST, instance = opportunity)
        if opportunity_form.is_valid():
            opportunity_form.save()
            return redirect('/')

    context = { 'opportunity_form' : opportunity_form }
    return render(request, 'volunteerUofG/updateOpportunity.html', context)

def deleteOpportunity(request, pk):
    opportunity = Opportunity.objects.get(id = pk)    

    if request.method == 'POST':
        opportunity.delete()           
        return redirect('/')

    context = { 'opportunity' : opportunity }
    return render(request, 'volunteerUofG/deleteOpportunity.html', context)

    
@login_required
def myAccount(request, pk):
    user = User.objects.get(id = pk)

    user_form = UserForm( instance = user)

    if(request.method == 'POST'):
        user_form = UserForm( request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/')
    context = {'user_form' : user_form}

    return render(request, 'volunteerUofG/myAccount.html', context)

    




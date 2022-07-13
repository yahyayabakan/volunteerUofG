from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "volunteerUofG/index.html")

def login(request):
    return render(request, "volunteerUofG/login.html")  

def faq(request):
    return render(request, "volunteerUofG/faq.html")      


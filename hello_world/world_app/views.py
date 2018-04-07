from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
def SayHello(request):
    return HttpResponse("Say Hello ....")

def SayWelcome(request):
    return HttpResponse("Welcome to my site ...")
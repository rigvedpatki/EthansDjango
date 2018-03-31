from django.shortcuts import render
# include template view
from django.views.generic import TemplateView

# Create your views here.

# Create HomeView class and inherit TemplateView
class HomeView(TemplateView):
    template_name = 'index.html'

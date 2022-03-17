from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class Home2PageView(TemplateView):
    template_name = 'home2.html'

class Home3PageView(TemplateView):
    template_name = 'home3.html'
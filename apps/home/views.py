from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name = 'home/index1.html'

class Home1(TemplateView):
    template_name = 'home/index2.html'
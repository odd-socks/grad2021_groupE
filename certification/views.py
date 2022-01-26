from re import template
from django.shortcuts import render
from django.views import generic
#from certification.models import CustomUser

# Create your views here.
#トップページ
class IndexView(generic.TemplateView):
     template_name = 'certification/index.html'

#施設トップページ
class FacilityView(generic.TemplateView):
     template_name = 'certification/facility.html'
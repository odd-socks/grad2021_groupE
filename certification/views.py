from re import template
from django.shortcuts import render
from django.views import generic

#from certification.models import CustomUser
#from django.contrib.auth.models import CusotmUser
#from allauth.account.forms import CustomSignupForm
#from django.contrib.auth.mixins import LoginRequiredMixin #アクセス権限→認証を促す



# Create your views here.
#トップページ
class IndexView(generic.TemplateView):
     template_name = 'certification/index.html'

#施設トップページ
class FacilityView(generic.TemplateView):
     template_name = 'certification/facility.html'


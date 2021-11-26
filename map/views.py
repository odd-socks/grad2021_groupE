from django.http.response import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import MapCreateForm
from .models import Facility, User

# Create your views here.
class TopView(generic.TemplateView):
    template_name = 'map/top.html'

class MapListView(generic.ListView):
    template_name = 'map/map_list.html'

class MapCreateView(generic.ListView):
    model = User
    template_name = 'map/map_create.html'
    success_url = reverse_lazy('map:map_create')
from django.shortcuts import render
from django.views import generic
from .models import Facility

# Create your views here.
class TopView(generic.TemplateView):
    template_name = "root/top.html"

# class MapSelectView(LoginRequiredMixin, generic.MapSelectView):
class MapSelectView(generic.ListView):
    model = Facility
    template_name = "root/map_select.html"

# class MapCreateView(LoginRequiredMixin, generic.MapCleateView):
class MapCreateView(generic.ListView):
    model = Facility
    template_name = "root/map_create.html"
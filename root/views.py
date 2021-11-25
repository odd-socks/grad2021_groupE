from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import Facility, User

# Create your views here.
class TopView(generic.TemplateView):
    template_name = "root/top.html"

class UserListView(ListView):
    model = User
    template_name = "root/user_list.html"
    
    # def get_queryset(self):
    #     roots = User.objects.filter(user=self.request.user).order_by('-created_at')
    #     return roots

class UserJsonView(BaseDatatableView):
    model = User
    columns = ['facility', 'name']
    # template_name = "root/map_create.html"
    # success_url = reverse_lazy('root:map_list')
    def map_create(self):
        return super().FILTER_ICONTAINS

    # def ajax_map_create(request):
    #     user_name = (request.post.get('user_name'))
    #     sort = User.objects.values_list('name', flat=True).get(name)
    #     data = {
    #         'sort':sort,
    #     }
    #     return JsonResponse(data)


    # def get_queryset(self):
    #     q_word = self.request.GET.get('query')
 
    #     if q_word:
    #         object_list = User.objects.filter(
    #             Q(name__icontains=q_word))
    #     else:
    #         object_list = User.objects.all()
    #     return object_list
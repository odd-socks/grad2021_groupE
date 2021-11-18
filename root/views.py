from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .forms import MapCreateForm
from .models import Facility, User

# Create your views here.
class TopView(generic.TemplateView):
    template_name = "root/top.html"

# class MapSelectView(LoginRequiredMixin, generic.MapSelectView):
class MapListView(generic.ListView):
    model = Facility
    template_name = "root/map_list.html"
    
    def get_queryset(self):
        roots = User.objects.filter(user=self.request.user).order_by('-created_at')
        return roots

# class MapCreateView(LoginRequiredMixin, generic.MapCleateView):
class MapCreateView(generic.ListView):
    model = User
    template_name = "root/map_create.html"
    form_class = MapCreateForm
    success_url = reverse_lazy('root:map_list')

    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = User.objects.filter(
                Q(name__icontains=q_word))
        else:
            object_list = User.objects.all()
        return object_list

    # def form_valid(self,form):
    #     user = form.save(commit=False)
    #     user.name = self.request.name
    #     user.save()
    #     messages.success(self.request,'ルートを作成しました。')
    #     return super().form_valid(form)

    # def form_invalid(self,form):
    #     messages.error(self.request,'ルートの作成に失敗しました。')
    #     return super().form_invalid(form)
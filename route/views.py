from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import MapCreateForm
from .models import Facility, User

# Create your views here.
class TopView(generic.TemplateView):
    template_name = 'route/top.html'

class MapListView(generic.ListView):
    template_name = 'route/map_list.html'

class MapCreateView(generic.ListView):
    # template_name = 'route/map_create.html'
    model = User
    # template_name = 'route/map_create.html'
    # form_class = MapCreateForm
    # success_url = reverse_lazy('route:map_list')

    def ajax_post_search(request):
        keyword = request.GET.get('address')
    
        # 検索キーワードがあればそれで絞り込み、なければ全ての記事
        # JSONシリアライズするには、Querysetをリストにする必要あり
        if keyword:
            user_list = [user.address for user in User.objects.filter(name__icontains=keyword)]  # nameにキーワードを含む。大文字小文字の区別なし
        else:
            user_list = [user.name for user in User.objects.all()]
    
        d = {
            'user_list': user_list,
        }
        return JsonResponse(d)


    # def get_queryset(self):
    #     q_word = self.request.GET.get('query')
 
    #     if q_word:
    #         object_list = User.objects.filter(
    #             Q(name__icontains=q_word))
    #     else:
    #         object_list = User.objects.all()
    #     return object_list


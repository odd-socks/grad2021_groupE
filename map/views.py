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
    
    def ajax_post_search(request):
        keyword = request.GET.get('name')

        # 検索キーワードがあればそれで絞り込み、なければ全ての記事
        # JSONシリアライズするには、Querysetをリストにする必要あり
        if keyword:
            name_list = [row.address for row in User.objects.filter(name__icontains=keyword)]  # タイトルにキーワードを含む。大文字小文字の区別なし
        else:
            name_list = [row.address for row in User.objects.order_by('facility').all()]

        d = {
            'name_list': name_list,
        }
        return JsonResponse(d)
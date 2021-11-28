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
    keyword = request.GET.get('user')
    # 検索キーワードがあればそれで絞り込み、なければ全ての記事
    # JSONシリアライズするには、Querysetをリストにする必要あり
    if keyword:
        name_list = [[column.name, column.address] for column in User.objects.filter(name__icontains=keyword)]  # nameにキーワードを含む。大文字小文字の区別なし
    else:
        # name_list = [column.name for column in User.objects.all()]
        name_list = ["一致する人物が見つかりませんでした。"]
    d = {
        'name_list': name_list,
    }
    return JsonResponse(d)
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Facility, User

# Create your views here.
class TopView(generic.TemplateView):
    template_name = 'map/top.html'

class MapListView(generic.ListView):
    template_name = 'map/map_list.html'

class UserList(generic.ListView):
    model = User
    
def ajax_post_search(request):
    keyword = request.GET.get('user')
    # 検索キーワードがあればそれで絞り込み、なければ全ての記事
    # JSONシリアライズするには、Querysetをリストにする必要あり
    if keyword:
        name_list = [[column.name, column.address] for column in User.objects.filter(name__icontains=keyword)]  # nameにキーワードを含む。大文字小文字の区別なし
    else:
        name_list = ["名前を入力してください。"]

    d = {
        'name_list': name_list
    }
    return JsonResponse(d)

def ajax_map_create(request):
    pick = request.Get.get('user')
    if pick:
        add_button = [[column.name, column.address] for column in User.objects.filter(name__icontains=keyword)]
    
    d = {
        'name_list': name_list
    }
    return JsonResponse(d)
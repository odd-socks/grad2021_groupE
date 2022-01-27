from django.http.response import JsonResponse
from django.http import JsonResponse, request
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse
from customer.models import User
from .models import Map
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser




# Create your views here.
class TopView(generic.TemplateView):
    template_name = 'map/top.html'



# class UserList(generic.ListView):
#     model = User
#     template_name = 'map/user_list.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
    #     context["message"] = self.request.GET.get('message')
    #     return context



@login_required
def user_list(request):
  user = request.user
  template_name = 'map/user_list.html'
  user_list = User.objects.filter(facility_id=user.id)
  context = {
    'user': user,
    'user_list': user_list,
  }
  return render(request, template_name, context)



def user_search(request):
    keyword = request.GET.get('user')

    if keyword:
        name_list = [[column.name, column.age, column.gender, column.address, column.carry_address] for column in User.objects.filter(name__icontains=keyword)]  # nameにキーワードを含む。大文字小文字の区別なし
        d = {'name_list': name_list}
    else:
        error = "名前を入力してください"
        d = {'error': error}
        
    return JsonResponse(d)



@login_required
def map_list(request):
  template_name = 'map/map_list.html'
  map_list = Map.objects.filter(facility_id=request.user.id)

  context = {
    'map_list': map_list,
    'waypoints': 'https://www.google.com/maps/dir/?api=1&waypoints=',
    'destination': '&destination='
  }

  return render(request, template_name, context)



def map_confirm(request):
    pointsString = request.GET.get('pointsString')
    input_name   = request.GET.get('input_name')
    waypoints    = request.GET.get('waypoints')
    destination    = request.GET.get('destination')
    
    data = {
        'pointsString': pointsString,
        'input_name': input_name,
        'waypoints': waypoints,
        'destination': destination
    }

    return render(request, 'map/map_confirm.html', data)



@login_required
def map_create(request):
    pointsString = request.POST.get('pointsString')
    input_name   = request.POST.get('input_name')
    waypoints    = request.POST.get('waypoints')
    destination    = request.POST.get('destination')
    
    # data = {
    #     'pointsString': pointsString,
    #     'input_name'  : input_name
    # }
    map_all = Map.objects.filter(name=input_name)
    if map_all:
        context = {
            'message'     : '※同じ名前のルートがすでに存在しています。',
            'input_name'  : input_name,
            'pointsString': pointsString,
            'waypoints'   : waypoints,
            'destination' : destination
        }
        return render(request, 'map/user_list.html', context)
    else:
        record = Map(name=input_name,route=pointsString,waypoints=waypoints,destination=destination,facility_id=request.user.id)
        record.save()
        return render(request, 'map/map_create.html', {'message': '送迎ルートを登録しました。'})

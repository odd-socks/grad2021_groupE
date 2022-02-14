from django.http.response import JsonResponse
from django.http import JsonResponse, request
from django.shortcuts import redirect, render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from customer.models import User
from .models import Routing
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.contrib import messages#メッセージフレームワーク




# Create your views here.
class TopView(generic.TemplateView):
     template_name = 'routing/top.html'



# class UserList(generic.ListView):
#     model = User
#     template_name = 'routing/user_list.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
    #     context["message"] = self.request.GET.get('message')
    #     return context



@login_required
def user_list(request):
    user = request.user
    template_name = 'routing/user_list.html'
    user_list = User.objects.filter(facility_id=user.id)
    context = {
    'user': user,
    'user_list': user_list,
    }
    return render(request, template_name, context)



def user_search(request):
    keyword = request.GET.get('user')

    if keyword:
        name_list = [[column.name, column.age, column.gender, column.address, column.carry_address, column.id] for column in User.objects.filter(name__icontains=keyword)]  # nameにキーワードを含む。大文字小文字の区別なし
        d = {'name_list': name_list}
    else:
        error = "名前を入力してください"
        d = {'error': error}
        
    return JsonResponse(d)



@login_required
def routing_list(request):
  template_name = 'routing/routing_list.html'
  routing_list = Routing.objects.filter(facility_id=request.user.id)

  context = {
    'routing_list': routing_list,
    'waypoints': 'https://www.google.com/maps/dir/?api=1&waypoints=',
    'destination': '&destination='
  }

  return render(request, template_name, context)



def confirm(request):
    pointsString = request.GET.get('pointsString')
    input_name   = request.GET.get('input_name')
    waypoints    = request.GET.get('waypoints')
    destination  = request.GET.get('destination')
    person_ids   = request.GET.get('person_ids')

    
    data = {
        'pointsString': pointsString,
        'input_name'  : input_name,
        'waypoints'   : waypoints,
        'destination' : destination,
        'person_ids'  : person_ids,
    }
    return render(request, 'routing/confirm.html', data)



@login_required
def create(request):
    pointsString = request.POST.get('pointsString')
    input_name   = request.POST.get('input_name')
    waypoints    = request.POST.get('waypoints')
    destination  = request.POST.get('destination')
    person_ids   = request.POST.get('person_ids').split(',')
    # print(person_ids)
    # data = {
    #     'pointsString': pointsString,
    #     'input_name'  : input_name
    # }
    routing_all = Routing.objects.filter(name=input_name)
    if routing_all:
        context = {
            'message'     : '※同じ名前のルートがすでに存在しています。',
            'input_name'  : input_name,
            'pointsString': pointsString,
            'waypoints'   : waypoints,
            'destination' : destination,
        }
        return render(request, 'routing/user_list.html', context)
    else:
        record = Routing(name=input_name,route=pointsString,waypoints=waypoints,destination=destination,facility_id=request.user.id)
        record.save()
        # person = User.objects.filter(id=person_ids)
        # d = {'person_ids':person_ids}
        for person_id in person_ids:
            person_id = int(person_id)
            result = User.objects.filter(id=person_id)
            for person in result:
                person.map_id = Routing.objects.last().id
                person.save()
        # print(person.name)
        # person = routing_id
    messages.success(request, 'ルートを登録しました')
    return render(request, 'certification/facility.html')

@login_required
def delete(request, route_id):
    """ ユーザーを削除 """
    route_id = get_object_or_404(Routing, id=route_id)
    route_id.delete()
    messages.success(request, 'ルートを削除しました')
    return redirect('certification:facility')

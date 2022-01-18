from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from .models import User
from django.shortcuts import render
# Create your views here.

# def index(request):
#     user_list = {'user': User.objects.all()}
#     return render(request, 'customer/index.html', user_list)
def index(request):
        user_list = User.objects.all()
        params = {'message' : 'ユーザー一覧' , 'data' : user_list}
        return render(request, 'customer/index.html' ,params)

def user_list(request: WSGIRequest) -> JsonResponse:
    """ ユーザー一覧を表示する """
    users = User.objects.all()
    user_list = [
        {"id": user.id, "name": user.name, "age": user.age} for user in users
    ]

    return JsonResponse({"user_list": user_list})


def user_create(request: WSGIRequest, user_id: int) -> JsonResponse:
    """ 新規にユーザーを作る """
    name = request.GET.get("name") or "No Name"
    age = request.GET.get("age") or "20"
    user = User(id=user_id, name=name)
    user.save()

    return JsonResponse({"id": user.id, "name": user.name, "age": user.age})

def user_update(request: WSGIRequest, user_id: int) -> JsonResponse:
    """ ユーザー情報を更新する """
    return JsonResponse({})


def user_delete(request: WSGIRequest, user_id: int) -> JsonResponse:
    """ ユーザーを削除する """
    return JsonResponse({})


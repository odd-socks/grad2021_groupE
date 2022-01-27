from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import User
from .forms import UserForm,SubUserForm
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
# Create your views here.

def toppage(request):
    return render(request, 'customer/toppage.html')

def index(request):
        """ ユーザーを一覧表示 """
        user_list = User.objects.all()
        params = {'message' : 'ユーザー一覧' , 'data' : user_list}
        return render(request, 'customer/index.html' ,params)

def new(request):
    """ ユーザーを追加 """
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer:list')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = UserForm()
    return render(request, 'customer/new.html', params)
 
def list(request):
    """ ユーザーを一覧表示 """
    user_list = User.objects.all()
    params = {'message': 'メンバーの一覧', 'data': user_list}
    return render(request, 'customer/list.html', params)

def detail(request, customer_id):
    """ ユーザー詳細 """
    customer_id = get_object_or_404(User, pk=customer_id)
    return render(request, 'customer/detail.html', {'data': customer_id})

@require_POST
def delete(request, customer_id):
    """ ユーザーを削除 """
    customer_id = get_object_or_404(User, id=customer_id)
    customer_id.delete()
    return redirect('customer:toppage')

def update(request, customer_id):
    """ ユーザーを編集 """
    customer_id = get_object_or_404(User, id=customer_id)
    if request.method == "POST":
        form = SubUserForm(request.POST, instance=customer_id)
        if form.is_valid():
            form.save()
            return redirect('customer:toppage')
    else:
        form = SubUserForm(instance=customer_id)
    return render(request, 'customer/update.html', {'form': form, 'data':customer_id })
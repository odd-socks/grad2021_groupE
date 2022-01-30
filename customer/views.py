from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import User
# from django.contrib.auth.models import User
from .forms import UserForm,SubUserForm
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def toppage(request):
    return render(request, 'customer/toppage.html')

@login_required
def index(request):
        """ ユーザーを一覧表示 """
        user_list = User.objects.all()
        params = {'message' : 'ユーザー一覧' , 'data' : user_list}
        return render(request, 'customer/index.html' ,params)

@login_required
def new(request):
    """ ユーザーを追加 """
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.facility_id = request.user.id
            new.save()
            return redirect('customer:list')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = UserForm()
    return render(request, 'customer/new.html', params)
 
@login_required
def list(request):
    """ ユーザーを一覧表示 """
    user_list = User.objects.filter(facility_id=request.user.id)
    params = {'message': 'メンバーの一覧', 'data': user_list}
    return render(request, 'customer/list.html', params)

@login_required
def detail(request, customer_id):
    """ ユーザー詳細 """
    customer_id = get_object_or_404(User, pk=customer_id)
    return render(request, 'customer/detail.html', {'data': customer_id})

@login_required
@require_POST
def delete(request, customer_id):
    """ ユーザーを削除 """
    customer_id = get_object_or_404(User, id=customer_id)
    customer_id.delete()
    return redirect('customer:toppage')

@login_required
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
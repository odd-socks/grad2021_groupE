from fileinput import filename
from itertools import count
from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from .forms import UserForm,SubUserForm
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from io import BytesIO
import base64
import qrcode
from django.contrib import messages#メッセージフレームワーク
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

            input_name = request.POST.get('name')
            input_password = request.POST.get('email')

            params = {
                'message': '',
                'input_name': input_name,
                'input_password': input_password
            }

            # url = 'http://127.0.0.1:8000/qrfunction/index?name='+input_name+'&email='+input_password
            # img = qrcode.make(url)  # QRコードを生成


            new = form.save(commit=False)
            new.facility_id = request.user.id
            new.password = make_password(input_password,input_name)
            new.save()

            # """保存するファイル名を作る"""
            # if User.objects.filter().exists():
            #     """ユーザーが一人でもいる場合の処理"""
            #     new_customer_id = User.objects.last().id
            #     new_customer_id = new_customer_id + 1

            #     """QRコードをフォルダに保存"""
            #     file_name = 'static/assets/img/qr_images/qr_img' + str(new_customer_id) + '.png'
            #     img.save(file_name)

            #     new.img_name = file_name


            # else:
            #     """ユーザーがいなかった時の処理"""
            #     new.save()
            #     new_customer_id = User.objects.last().id

            #     """QRコードをフォルダに保存"""
            #     file_name = 'static/assets/img/qr_images/qr_img' + str(new_customer_id) + '.png'
            #     img.save(file_name)

            #     new.img_name = file_name
            #     new.save()

            # """利用者一覧に遷移"""
            messages.success(request, '利用者を登録しました。')
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
    messages.success(request, '利用者を削除しました。')
    return redirect('customer:toppage')

@login_required
def update(request, customer_id):
    """ ユーザーを編集 """
    customer_id = get_object_or_404(User, id=customer_id)
    if request.method == "POST":
        form = SubUserForm(request.POST, instance=customer_id)
        if form.is_valid():
            form.save()
            messages.success(request, '利用者情報を保存しました。')
            return redirect('customer:toppage')
    else:
        form = SubUserForm(instance=customer_id)
    return render(request, 'customer/update.html', {'form': form, 'data':customer_id })

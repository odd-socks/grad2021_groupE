# Create your views here.

from distutils.core import run_setup
from operator import truediv
from tkinter.messagebox import NO
from unittest import result
from unittest import result
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, get_object_or_404, redirect
from customer.models import User
from .models import CarryLog
from .forms import QrFuncForm
from django import forms

""" 追加 """
from django.contrib import messages

def search(request):
    """ただの検索"""
    form = QrFuncForm()

    return render(request, 'qrfunction/search.html')


def registration(request):
    """送迎完了"""
    input_name = request.POST.get('name')
    input_password = request.POST.get('password')
    print(input_name)
    print(input_password)
    try_pass = make_password(input_password,input_name)
    print(try_pass)
    # true_pass = check_password(try_pass)
#----------------------------------------------------------------------------------------------------
    #送迎中判定欄の反転処理
    results = User.objects.filter(name=input_name, password=try_pass)  # Userテーブルから複数条件で検索
    for result in results:
        result.is_carryed = False
        result.save()
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
    #送迎ログの登録
    for log_catch in results:
        log = CarryLog(email=log_catch.email)
        log.save()
#----------------------------------------------------------------------------------------------------
    return render(request, 'qrfunction/registration.html')


def index(request):
    """ユーザー判定"""
    input_name = request.GET.get('name')
    input_password = request.GET.get('password')

    # print(input_name)
    # print(input_password)
    fill= User.objects.filter(name=input_name)
    # fill= User.objects.filter(name='小泉')
    # print(fill)
    # results = User.objects.filter(name=input_name, password=input_password)  # Userテーブルから複数条件で検索
    # print(results)    
    # print(try_pass)
    
    if not fill:
        return render(request,'qrfunction/search.html',{'error':'名前が間違っています。'})
        
    else:

        for result in fill:

            if request.GET.get('password') != result.password:
                print(request.GET.get('password'))
                print(result.password)
            # if check_password(result.password,result.name) != check_password(input_password,input_name) :
                return render(request,'qrfunction/search.html',{'error':'パスワードが間違っています。'})

            # elif result.is_carryed == False:
            #     return render(request,'qrfunction/search.html', {'error':'送迎中ではありません'})

            elif result.is_carryed == True:
                return render(request,'qrfunction/index.html', {'data':fill})
    
    return render(request,'qrfunction/search.html')

    # results = User.objects.filter(name=input_name, email=input_password)  # Userテーブルから複数条件で検索


    # if not results:
    #     return render(request,'qrfunction/search.html',{'error':'名前もしくはメールアドレスが間違っています'})
    # else:
    #     for result in results:
    #         if result.is_carryed == False:
    #             return render(request,'qrfunction/search.html', {'error':'送迎中ではありません'})
    #         elif result.is_carryed == True:
    #             return render(request, 'qrfunction/index.html', {'data':results})


def detail(request, customer_id):
    """ ユーザー詳細 """
    customer_id = get_object_or_404(User, pk=customer_id)
    return render(request, 'qrfunction/detail.html', {'data': customer_id})

def newpass(request):
    pass
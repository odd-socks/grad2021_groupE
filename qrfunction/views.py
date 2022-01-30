# Create your views here.

from distutils.core import run_setup
from tkinter.messagebox import NO
from unittest import result
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
    input_email= request.POST.get('email')

#----------------------------------------------------------------------------------------------------
    #送迎中判定欄の反転処理
    results = User.objects.filter(name=input_name, email=input_email)  # Userテーブルから複数条件で検索
    for result in results:
        result.is_carryed = False
        result.save()
        # print(result.is_carryed)
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
    #送迎ログの登録
    log = CarryLog(email=input_email)
    log.save()
#----------------------------------------------------------------------------------------------------
    return render(request, 'qrfunction/registration.html')


def index(request):
    """ユーザー判定"""
    input_name = request.POST.get('name')
    input_email= request.POST.get('email')

    results = User.objects.filter(name=input_name, email=input_email)  # Userテーブルから複数条件で検索
    # print(results)  # ターミナルに結果を出力
    if not results:
        return render(request,'qrfunction/search.html',{'error':'名前もしくはメールアドレスが間違っています'})
    else:
        for result in results:
            if result.is_carryed == False:
                return render(request,'qrfunction/search.html', {'error':'送迎中ではありません'})
            elif result.is_carryed == True:
                return render(request, 'qrfunction/index.html', {'data':results})


def detail(request, customer_id):
    """ ユーザー詳細 """
    customer_id = get_object_or_404(User, pk=customer_id)
    return render(request, 'qrfunction/detail.html', {'data': customer_id})
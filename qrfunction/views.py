# Create your views here.

from django.shortcuts import render, get_object_or_404
from customer.models import User
from .models import CarryLog
from .forms import QrFuncForm
from django import forms

""" 追加 """
from django.contrib import messages

def search(request):
    form = QrFuncForm()

    return render(request, 'qrfunction/search.html')



def registration(request):
    input_name = request.GET.get('name')
    input_email= request.GET.get('email')

#----------------------------------------------------------------------------------------------------
    #送迎中判定欄の反転処理
    results = User.objects.filter(name=input_name, email=input_email)  # Userテーブルから複数条件で検索
    for result in results:
        result.is_carryed = True
        result.save()
        print(result.is_carryed)
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
    #送迎ログの登録
    log = CarryLog(email=input_email)
    log.save()
#----------------------------------------------------------------------------------------------------
    return render(request, 'qrfunction/registration.html')



def index(request):
    input_name = request.GET.get('name')
    input_email= request.GET.get('email')

    results = User.objects.filter(name=input_name, email=input_email)  # Userテーブルから複数条件で検索
    print(results)  # ターミナルに結果を出力

    return render(request, 'qrfunction/index.html', {'data':results})




def detail(request, customer_id):
    """ ユーザー詳細 """
    customer_id = get_object_or_404(User, pk=customer_id)
    return render(request, 'qrfunction/detail.html', {'data': customer_id})
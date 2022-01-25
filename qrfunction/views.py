# Create your views here.

from django.shortcuts import render, get_object_or_404
from customer.models import User
""" 追加 """
from django.contrib import messages
from django.db.models import Q

def index(request):
    # """ 検索機能の処理 """
    # users = User.objects.filter(email=input_email)
    # keyword = request.GET.get('keyword')

    # if keyword:
    #     customer_id = user.filter(
    #              (name__iexact=keyword), (email__iexact=keyword)
    #            )
    #     messages.success(request, '「{}」の検索結果'.format(keyword))

    # return render(request, 'qrfunction/index.html', {'data' : users })

#ore area------------------------------------------------------
    input_name  = '水口'
    input_email = 'ksw2070118@stu.o-hara.ac.jp'
    result = {}


    users = User.objects.filter(email=input_email)
    # for user in users:
    #     if user.email == address:
    #         result = {
    #             'name' : user.name,
    #             'email': user.email,
    #             'age'  : user.age
    #         }
    return render(request, 'qrfunction/index.html', {'data':users})
#ore area------------------------------------------------------






def detail(request, customer_id):
    """ ユーザー詳細 """
    customer_id = get_object_or_404(User, pk=customer_id)
    return render(request, 'qrfunction/detail.html', {'data': customer_id})
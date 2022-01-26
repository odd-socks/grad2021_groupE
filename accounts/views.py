from django.shortcuts import render,redirect
from .forms import FacilityUserForm
# Create your views here.

def NewFacilityUser(request):
    """ ユーザーを追加 """
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = FacilityUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/facility_list')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = FacilityUserForm()
    return render(request, 'accounts/create.html', params)

def FacilityUserList(request):
    """ ユーザーを一覧表示 """
    user_list = NewFacilityUser.objects.all()
    params = {'message': '施設の一覧', 'data': user_list}
    return render(request, 'accounts/facility_list.html', params)
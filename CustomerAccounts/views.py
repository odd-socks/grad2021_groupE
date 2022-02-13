from django.shortcuts import render, redirect
from customer.models import User
from django.contrib.auth.hashers import make_password, check_password
from io import BytesIO
import base64
import qrcode
# Create your views here.

def CustomerLogin(request):
    input_name = request.POST.get('name')
    input_password = request.POST.get('password')

    request.session['name'] = input_name
    request.session['password'] = input_password

    # print(request.session['name'])
    # print(request.session['password'])
    # if request.session['name']['password'] == True:
    #     print(request.settion['name'])

    fill= User.objects.filter(name=input_name)

    try_pass = make_password(input_password,input_name)
    
    if (not input_name )and(not input_password):
        return render(request,'CustomerAccounts/customer_login.html')

    if not fill:
        return render(request,'CustomerAccounts/customer_login.html',{'error':'名前が間違っています。'})

    else:

        for result in fill:

            if check_password(input_password,result.password) == False:
                return render(request,'CustomerAccounts/customer_login.html',{'error':'パスワードが間違っています。'})

            elif input_password == result.email:
                return render(request,'CustomerAccounts/customer_login_sertif.html',{'msg':'初回パスワード変更を行うため、もう一度ログインしてください。'})
                
            elif check_password(input_password,result.email) == False:
                request.session['name'] = input_name
                request.session['password'] = input_password
                return redirect('certification:underwriter')
    
    return render(request,'CustomerAccounts/customer_login.html')

def CustomerLoginSertif(request):
    input_name = request.POST.get('name')
    input_email = request.POST.get('email')

    fill= User.objects.filter(name=input_name)

    try_pass = make_password(input_email,input_name)
    
    if (not input_name )and(not input_email):
        return render(request,'CustomerAccounts/customer_login_sertif.html')

    if not fill:
        return render(request,'CustomerAccounts/customer_login_sertif.html',{'error':'名前が間違っています。'})

    else:

        for result in fill:

            if input_email == result.email:
                return render(request,'CustomerAccounts/customer_login.html',{'error':'メールアドレスが間違っています。'})

            elif check_password(input_email,result.password):
                return render(request, 'CustomerAccounts/customer_login.html',{'error':'あなたは初回ログインではありません。'})
            
            else:
                return render(request,'CustomerAccounts/customer_login_pass.html',{'data':fill})

def CustomerLoginPass(request):
    input_password = request.POST.get('password')
    input_password_try = request.POST.get('password_again')

    input_name = request.POST.get('name')
    input_email = request.POST.get('email')
    print(input_name)
    print(input_email)
    fill = User.objects.filter(name = input_name, email = input_email)
    print(fill)

    """自作バリデーション"""
    if (not input_password) and (not input_password_try):
        return render(request,'CustomerAccounts/customer_login_pass.html',{'data':fill})

    elif (not input_password):
        return render(request,'CustomerAccounts/customer_login_pass.html',{'msg':'パスワードが空欄です。','data':fill})

    elif (not input_password_try):
        return render(request, 'CustomerAccounts/customer_login_pass.html',{'msg':'パスワード確認を入力してください。','data':fill})


    if input_password != input_password_try:
        return render(request,'CustomerAccounts/customer_login_pass.html',{'msg':'入力されたパスワードが同じではありません。','data':fill})

    if input_password == input_password_try:
        """入力されたパスワードと確認パスワードが合致した場合、入力パスワードを暗号化しDBへ保存、QRコード生成"""
        dark_pass = make_password(input_password,input_name)
        fill.password = dark_pass

        url = 'http://127.0.0.1:8000/CustomerAccounts/customer_login_pass?name='+input_name+'&password='+input_password
        img = qrcode.make(url)  # QRコードを生成


        for result in fill:
            
            file_name = 'static/assets/img/qr_images/qr_img' + str(result.id) + '.png'
            img.save(file_name)

            result.img_name = file_name
            result.password = dark_pass
            result.save()

        request.session['name'] = input_name
        request.session['password'] = input_password

        redirect('certification:underwriter')

    """ここまで"""
    return render(request, 'Certification/underwriter.html')

def CustomerLogOut(request):
    session_name_qr = request.session['name']
    session_pass_qr = request.session['password']

    # if  not session_name_qr and not session_pass_qr:
    del request.session['name']
    del request.session['password']

    request.session['name'] = None
    request.session['password'] = None
        
    return redirect('certification:underwriter')
    # else:
    #     return render(request, 'Certification/underwriter.html' ,{'msg':'ログインしていません。'})


def CustomerQrcode(request):
    # print(request.session["name"])
    # if 'name' in request.session:
    #     # request.session["name"] = None
    #     # request.session["password"] = None
    #     print(request.session["name"])
    #     pass

    # if request.session["name"] == None:


    #     request.session['name']
    #     request.session['password']


    #     del request.session['name']
    #     del request.session['password']
    #     return render(request,'CustomerAccounts/customer_login.html',{'error' : 'ログインしていません。'})
    # # elif (request.session['name'] is None):
    # #     return render(request,'CustomerAccounts/customer_login.html',{'error' : 'ログインしていません。'})
    # else:
    #     pass

    session_name_qr = request.session['name']
    session_pass_qr = request.session['password']
        
    # print(request.session['name'])
    # print(request.session['password'])
    # print(session_name_qr)
    # print(session_pass_qr)
    # dark_pass = make_password(session_pass_qr,session_name_qr)
    url = 'http://127.0.0.1:8000/qrfunction/index?name='+session_name_qr+'&password='+session_pass_qr
    print(url)
    session_qr_img = qrcode.make(url)  # QRコードを生成
    buffer = BytesIO()
    session_qr_img.save(buffer, format="PNG")
    session_qr_img = base64.b64encode(buffer.getvalue()).decode().replace("'", "")

    return render(request, 'CustomerAccounts/customer_qrcode.html',{'session': request.session,'session_qr':session_qr_img})
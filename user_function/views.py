from nis import maps
from django.shortcuts import render
from customer.models import User
# from map.models import Map



def certification(request):
  return render(request, 'user_function/certification.html')






def show_map(request):
  input_name = request.POST.get('name')
  input_email= request.POST.get('email')

  results = User.objects.filter(name=input_name, email=input_email)  # Userテーブルから複数条件で検索

  if not results:
      return render(request,'user_function/certification.html',{'error':'名前もしくはメールアドレスが間違っています'})
  else:
      for result in results:
          if result.is_carryed == False:
              return render(request,'user_function/certification.html', {'error':'送迎中ではありません'})
          elif result.is_carryed == True:
              print(result.map_id)
              # routeInfo = Map.objects.get(id=result.map_id)
              # context = {'route': routeInfo.route}
              return render(request, 'user_function/show_map.html', {'data':result})
  
  
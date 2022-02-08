from re import template
from django.shortcuts import render
from django.views import generic

#from certification.models import CustomUser
#from django.contrib.auth.models import CusotmUser
#from allauth.account.forms import CustomSignupForm
#from django.contrib.auth.mixins import LoginRequiredMixin #アクセス権限→認証を促す

import qrcode
import base64
from io import BytesIO
from django.shortcuts import render



# Create your views here.
#トップページ
class IndexView(generic.TemplateView):
     template_name = 'certification/index.html'

#施設トップページ
class FacilityView(generic.TemplateView):
     template_name = 'certification/facility.html'

#引受人トップページ
class Customer_mapView(generic.TemplateView):
     template_name = 'certification/customer_map.html'


#QRコード
def qrView(request):
  template_name = 'certification/qr.html'
  user_id = 1  # 施設_id
  
  # url = 'https://qrcode/' + str(user_id)  # QRコードに保存したいサイトのURL
  url = 'http://127.0.0.1:8000/qrfunction/'
  img = qrcode.make(url)  # QRコードを生成

  buffer = BytesIO()
  img.save(buffer, format="PNG")
  qr = base64.b64encode(buffer.getvalue()).decode().replace("'", "")
  context = {'qr': qr}

  return render(request, template_name, context)


from map.models import *

import json
from django.shortcuts import render

# def index_show(request):
#     return render(request,'customer_map.html') 

def customer_map_request(request):
    data = {
        'sample1': request.GET.get(map.waypoints),
        'sample2': request.GET.get(map.destination),
    }
    return render(request, "customer_map.html", {'data_json': json.dumps(data)})
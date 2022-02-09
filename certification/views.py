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
from django.contrib.auth.decorators import login_required




# Create your views here.
#トップページ
class IndexView(generic.TemplateView):
     template_name = 'certification/index.html'

#施設トップページ
class FacilityView(generic.TemplateView):
     template_name = 'certification/facility.html'

#引受人トップページ
class UnderwriterView(generic.TemplateView):
     template_name = 'certification/underwriter.html'


#QRコード
@login_required
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
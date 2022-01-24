from django.core.signing import TimestampSigner,BadSignature,SignatureExpired
from django.shortcuts import render
from django.views import View

import random
import string
from datetime import timedelta

EXPIRED_SECONDS = 5

class IndexView(View):
    template_name = 'timestamp_signer/index.html'
    timestamp_signer = TimestampSigner()

    def get_random_chars(self,char_num=30):
         return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(char_num)])

    def get(self,request,token=None):
        context = {}
        context['expired_seconds'] = EXPIRED_SECONDS

        if token:
            try:
                unsigned_token = self.timestamp_signer.unsign(
                    token,
                    max_age=timedelta(seconds=EXPIRED_SECONDS)
                )
                context['message'] = '有効なトークンです!!!'
            except SignatureExpired:
                context['message'] = 'このトークンは期限切れです。'
            except BadSignature:
                context['message'] = 'トークンが正しくありません。'

        return render(request, self.template_name, context)

    def post(self,request):
        context = {}
        context['expired_seconds'] = EXPIRED_SECONDS
        token = self.get_random_chars()
        token_signed = self.timestamp_signer.sign(token)
        context['token_signed'] = token_signed
        return render(request, self.template_name, context)
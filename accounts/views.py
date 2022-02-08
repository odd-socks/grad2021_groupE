from django.shortcuts import render
from certification.models import CustomUser
# Create your views here.

from django.core.mail import send_mail

def notify(request):
	subject = "題名"
	message = "本文"
	from_email = "e.ohno331@gmail.com"
	recipient_list = [
		"ksw2070331@stu.o-hara.ac.jp"
	]
	send_mail(subject, message, from_email, recipient_list)
	return render(request, 'app/index.html')
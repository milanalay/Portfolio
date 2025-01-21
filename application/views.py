from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages




def home_view(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')

		email_message = email + '' + ':' + '' + message

		try:
			client = ContactMe.objects.create(name=name, email=email, message=message)
			client.save()
			name = str(name)
			email_message = str(email_message)
			
			# send_mail_to_me(name, email_message)
			return HttpResponseRedirect('/thankyou')
		except Exception as e:
			print(e)
	else:
		None
	return render(request, "index.html", {})



def thankyou(request):
	return render(request, 'thankyou.html', {})




def send_mail_to_me(name, email_message):
	subject = name
	message = email_message
	from_email = settings.EMAIL_HOST_USER
	recipient_list = ['milanale.network@gmail.com']
	send_mail(subject, message, from_email, recipient_list)
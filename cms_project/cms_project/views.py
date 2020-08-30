from django.shortcuts import render
from .models import ContactUsQuery
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def ContactFormView(request):
	print(request)
	obj = ContactUsQuery.objects.create(
			f_name=request.POST.get('fnane'),
			email=request.POST.get('email'),
			message=request.POST.get('message'),
		)
	obj.save()
	html = "<center><div class=\"container\"><h1>Thanks for Contacting us<br>Return to <a href=\"/\">Home</a></h1></div></center>"
	return HttpResponse(html)

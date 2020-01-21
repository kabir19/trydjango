from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World!!!</h1>")
	return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about me",
		"this_is_true": True,
		"my_number": 1234,
		"my_list": [123, 456, 321, "Abc"]
	}
	return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World!!!</h1>")
	return render(request, "contact.html", {})
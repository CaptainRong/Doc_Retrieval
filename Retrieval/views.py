from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    print("try to connect")
    return HttpResponse('<h1>Hello World!</h1>')

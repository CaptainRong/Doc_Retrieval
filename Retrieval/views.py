from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    print("try to connect")
    return render(request,'index.html')

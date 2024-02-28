from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    print("try to connect")
    data = {
        'title': '科技文献大模型',

    }
    return render(request, 'index.html', data)


def chat(request):
    context = {
        'title': 'a main view'
    }

    return render(request, 'main.html',context)


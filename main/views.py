from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        'heading': 'Главная',
    }
    return render(request, 'main/index.html', data)

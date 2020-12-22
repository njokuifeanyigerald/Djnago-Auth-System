from django.shortcuts import render


def home(request):
    context = {
        "title": 'home'
    }
    return render(request, 'accounts/home.html', context)

def login(request):
    context = {
        "title": 'login'
    }
    return render(request, 'accounts/login.html', context)

def register(request):
    context = {
        "title": 'register'
    }
    return render(request, 'accounts/register.html', context)


from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate


@login_required(login_url='login')
def home(request):
    context = {
        "title": 'home'
    }
    return render(request, 'accounts/home.html', context)

def loginUser(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Username or Password is Incorrect")
    context = {
        "title": 'login'
    }
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form  = UserCreateForm()
    # user = User.objects.get(email=form.email)
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():

            # if user.exists():
            #     context = {"user": "email already exists"}

            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account created successfully ' + user)
            return redirect("login")
    context = {
        "form": form,
        "title": 'register'
    }
    return render(request, 'accounts/register.html', context)


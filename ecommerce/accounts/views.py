from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import *
# from django.contrib.auth.views import LoginView

# Create your views here.
def user_login(request):
    context = {}
    if request.method == 'GET':
        context['form'] = AuthenticationForm()
        return render(request, 'accounts/login.html', context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            context['form'] = form
            return render(request, 'accounts/login.html', context)

def register(request):
    context = {}
    if request.method == 'GET':
        context['form'] = UserRegistrationForm()
        return render(request, 'accounts/register.html', context)
    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        else:
            context['form'] = form
            return render(request, 'accounts/register.html', context)

def user_logout(request):
    logout(request)
    return redirect('/')
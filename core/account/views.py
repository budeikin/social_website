from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('you logged in successfully')
                else:
                    return HttpResponse('your account is not active')
            else:
                return HttpResponse('this user does not exist')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required(login_url='http://127.0.0.1:8000/accounts/login/')
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

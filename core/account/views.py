from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('you logged in successfully')
#                 else:
#                     return HttpResponse('your account is not active')
#             else:
#                 return HttpResponse('this user does not exist')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password2'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

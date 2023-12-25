from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required

from .models import Profile


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
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'user': user, 'profile': profile})


@login_required
def edit(request):
    if request.method == 'POST':
        user_edit_form = UserEditForm(instance=request.user, data=request.POST)
        profile_edit_form = ProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html',
                  {'user_edit_form': user_edit_form, 'profile_edit_form': profile_edit_form})

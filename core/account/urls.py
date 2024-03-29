from django.urls import path
from .views import dashboard, register, edit, user_detail, user_list, user_follow
from django.contrib.auth import views as auth_views

# app_name = 'account'

urlpatterns = [
    # register
    path('register/', register, name='register'),
    # login & logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # change password
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-change/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # dashboard
    path('', dashboard, name='dashboard'),
    # edit profile and user info
    path('edit/', edit, name='edit'),
    path('users/', user_list, name='user_list'),
    path('users/follow/', user_follow, name='user_follow'),
    path('users/<username>/', user_detail, name='user_detail'),

]

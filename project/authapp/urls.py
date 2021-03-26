from django.urls import path, include

from . import views

app_name = 'authapp'

urlpatterns = [
    path('registration/', views.UserCreateView.as_view(), name='registration'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('success/', views.success, name='success'),

    # reset password
    path('reset_password/', views.PasswordCustomResetView.as_view(), name='password_reset'),
    # path('reset_password_sent/', views.success, name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', views.PasswordResetConfirmCustomView.as_view(), name='password_reset_confirm'),
    # path('reset_password/', views.PasswordCustomResetView.as_view(), name='password_reset'),

]
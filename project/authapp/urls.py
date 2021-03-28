from django.urls import path

from . import views

app_name = 'authapp'

urlpatterns = [
    path('registration/', views.UserCreateView.as_view(), name='registration'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('success/', views.success, name='success'),
    path('delete_user/<pk>/', views.UserDeleteView.as_view(), name='delete_user'),

    # reset password
    path('reset_password/', views.PasswordCustomResetView.as_view(), name='password_reset'),
    path('reset_password_confirm/<uidb64>/<token>/',
         views.PasswordResetConfirmCustomView.as_view(),
         name='password_reset_confirm'),

]
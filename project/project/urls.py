from django.urls import path, include

from authapp import views as authapp

urlpatterns = [
    path('', authapp.LoginFormView.as_view(), name="index"),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('admin/', include('adminapp.urls', namespace='adminapp')),
    path('api/', include('api.urls', namespace='api')),
]

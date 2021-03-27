from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('djnago_admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('admin/', include('adminapp.urls', namespace='adminapp')),
    path('api/', include('api.urls', namespace='api')),
]

from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [

    path('', views.admin_index_view, name='admin_index'),
    path('user/<pk>', views.user_update_view, name='user_update'),

]
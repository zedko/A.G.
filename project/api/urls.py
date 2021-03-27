from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [

    path('generate/', views.generate_api_token, name='generate'),
    path('method/', views.method_rest_api_po_zaprosu_s_secret_kluchom, name='method'),

]
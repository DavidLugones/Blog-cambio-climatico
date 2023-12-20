from django.urls import path
from . import views

app_name = 'informate'

urlpatterns = [
    path('', views.Home_Informate, name="h_informate"),
    
]
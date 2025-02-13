from django.urls import path
from rango import views

app_name = 'rango'  # App namespace

urlpatterns = [
    path('', views.index, name='index'),  # Maps /rango/ to views.index
]


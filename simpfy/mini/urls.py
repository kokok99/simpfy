from django.urls import path
from . import views

urlpatterns = [
    path('mini-index', views.minindex, name='mini-index'),
    path('2048', views.dua, name="2048"),
    path('ttt', views.ttt, name="ttt"),
    path('hec', views.hec, name="hec"),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('tools-index', views.tools_index, name='tools-index'),
    path('tools-rembg', views.tools_rembg, name='tools-rembg'),
    path('remdel/<int:pk>', views.delete_rembg, name='remdel'),
]
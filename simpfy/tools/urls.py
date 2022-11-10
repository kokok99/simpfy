from django.urls import path
from . import views

urlpatterns = [
    path('tools-index', views.tools_index, name='tools-index'),
    path('tools-rembg', views.tools_rembg, name='tools-rembg'),
    path('remdel/<int:pk>', views.delete_rembg, name='remdel'),
    path('ytvid', views.yt2mp3, name='ytvid'),
    path('mpdel', views.delmp3, name="mpdel"),
    path('yt', views.yt, name='yt'),
    path('ytdel', views.delyt, name="ytdel"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload', views.upload , name='upload'),
    path('like-post', views.like_post , name="like-post"),
    path('delete_post/<str:pk>', views.delete_post, name="delete_post"),
]
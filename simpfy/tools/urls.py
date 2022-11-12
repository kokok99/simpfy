from django.urls import path
from . import views

urlpatterns = [
    path('tools-index', views.tools_index, name='tools-index'),
    path('wolf', views.wolf, name="wolf"),
    path('wolfdel/<int:pk>', views.wolfdel, name="wolfdel"),
]
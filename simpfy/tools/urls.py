from django.urls import path
from . import views

urlpatterns = [
    path('tools-index', views.tools_index, name='tools-index'),
    path('wolf', views.wolf, name="wolf"),
    path('wolfmath', views.wolfmath, name="wolfmath"),
    path('wolfweather', views.wolfweather, name="wolfweather"),
    path('wolfdel/<int:pk>', views.wolfdel, name="wolfdel"),
    path('wolfweatherdel/<int:pk>', views.wolfweatherdel, name="wolfweatherdel"),
    path('wolfmathdel/<int:pk>', views.wolfmathdel, name="wolfmathdel"),
    path('wiki', views.wiki, name="wiki"),
    path('wikidel/<int:pk>', views.wikidel, name="wikidel"),
    path('wikihow', views.wikihow, name="wikihow"),
    path('wikihowres/<int:pk>', views.wikihowres, name="wikihowres"),
    path('wikihowdel/<int:pk>', views.wikihowdel, name="wikihowdel"),
    path('qr', views.qr, name="qr"),
    path('bar', views.bar, name="bar"),
    path('hist', views.hist, name="hist"),
    path('line', views.line, name="line")
]
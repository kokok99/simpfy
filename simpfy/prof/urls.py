from django.urls import path
from . import views

urlpatterns = [

    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('settings', views.settings, name="settings"),
    path('profile/follow/<str:pk>/<int:opt>', views.follow , name="follow"),
    path('remove/<int:pk>', views.remove_pic, name="remove"),
]
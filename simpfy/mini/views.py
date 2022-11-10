from django.shortcuts import render
from prof.models import Profile
from django.contrib.auth.models import User, auth

# Create your views here.
def minindex(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()

    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
    }
    return render(request, 'mini/mini-games.html', context)

def dua(request):
    return render(request, 'mini/2048.html')

def ttt(request):
    return render(request, 'mini/ttt.html')

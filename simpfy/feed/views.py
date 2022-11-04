from django.shortcuts import render
from django.contrib.auth.models import User, auth
from .models import Feed, Likes
from prof.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    
    post = Feed.objects.all()
    
    context = {
        'user_profile':user_profile,
        'posts': post,
    }
    return render(request, 'feed/index.html', context)

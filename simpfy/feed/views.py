from django.shortcuts import render, redirect
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
    all_user = Profile.objects.all()

    
    post = Feed.objects.all()
    
    context = {
        'user_profile':user_profile,
        'posts': post,
        'all_user' : all_user,
    }
    return render(request, 'feed/index.html', context)

#---------------------------POSTING START-------------------------------------------------------
@login_required(login_url='signin')
def upload(request):
    
    if request.method == 'POST':
        user = request.user
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        text = request.POST['text']
        
        user_model = User.objects.get(username=user)
        
        new_post = Feed.objects.create(user=user_model, image=image, caption=caption, text=text)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Feed, Likes
from prof.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

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
        captionimg = request.POST['captionimg']
        captionvid = request.POST['captionvid']
        text = request.POST['text']
        video = request.FILES.get('video_upload')
        
        user_model = User.objects.get(username=user)
        
        if captionvid != None and video != None:
            new_post = Feed.objects.create(user=user_model, video=video, captionvid=captionvid)
            new_post.save()
            return redirect('/')
        elif image != None and captionimg != None:
            new_post = Feed.objects.create(user=user_model, image=image, captionimg=captionimg)
            new_post.save()
            return redirect('/')
        elif text != None:
            new_post = Feed.objects.create(user=user_model, text=text)
            new_post.save()
            return redirect('/')
        elif image == None and captionimg == None and captionvid == None and video == None and text == None:
            messages.info(request, 'No Post to post')
            return redirect('/')
        
    else:
        return redirect('/')

def delete_post(request, pk):
    user = request.user.username
    posts = Feed.objects.get(id=pk)
    image = posts.image
    video = posts.video
    fs = FileSystemStorage()
    if image:
        fs.delete(image.name)
    elif video:
        fs.delete(video.name)
    
    posts.delete()

    return redirect('/profile/'+user)


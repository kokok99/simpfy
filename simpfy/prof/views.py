from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile, Follow
from feed.models import Feed, Likes
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

#SIGNUP FUNCTION-------------------------------------------------------------------------
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()   
                
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)  
                new_profile.save() 
                return redirect('login')
        else:
            messages.info(request, "Password not match")
            return redirect('signup')
    else:
        return render(request, 'feed/signup.html')

#LOGIN FUCNTION------------------------------------------------------------------------
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'feed/login.html')

#LOGOUT FUNCTION-----------------------------------
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

#PROFILE FUNCTION------------------------------------------------
@login_required(login_url='login')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Feed.objects.all().filter(user=user_profile)
    user_post_len = len(user_posts)
    following_count = Follow.objects.filter(follower=user_object).count()
    followers_count = Follow.objects.filter(following=user_object).count()
    follow_status = Follow.objects.filter(following=user_object, follower=request.user).exists()

    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    
 

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_req' : user_req,
        'user_posts' : user_posts,
        'user_post_len' : user_post_len,
        'user_request' : user_request,
        'following_count' : following_count,
        'followers_count' : followers_count,
        'follow_status' : follow_status
    }

    return render(request, 'feed/profile.html', context)

#EDIT PROFILE FUNCTION------------------------------------------------
@login_required(login_url='login')
def settings(request):
    
    user_profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            bio = request.POST['bio']
            location = request.POST['location']
            fname = request.POST['fname']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.fname = fname
            user_profile.save()
            
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            fname = request.POST['fname']
            
            user_profile.image = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.fname = fname
            user_profile.save()
        
        return redirect('settings')
    
    context = {
        'user_profile' : user_profile,
    }
             
    return render(request, 'feed/settings.html', context)

#FOLLOW FUNCTION------------------------------------------------------------------------
@login_required(login_url='login')
def follow(request, pk, opt):
    user = User.objects.get(username=request.user)
    following = User.objects.get(username=pk)
    current = following.username
    if int(opt) == 1:
        follow = Follow.objects.create(follower=user, following=following)
        follow.save
        return redirect('/profile/'+current)
    else:
        unfollow = Follow.objects.filter(follower=user, following=following).first()
        unfollow.delete()
        return redirect('/profile/'+current)
     
def remove_pic(request, pk):
    user = request.user.username
    pic = Profile.objects.get(id=pk)
    pics = pic.image
    picname = pics.name
    if picname != "blank.png":
        fs = FileSystemStorage()
        fs.delete(pics.name)
        pics.delete()
        new_pic = fs.generate_filename('blank.png')
        pic.image = new_pic
        pic.save()
        return redirect('/profile/'+user)
    else:
        return redirect('/profile/'+user)
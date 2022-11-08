from django.shortcuts import render, redirect
from rembg import remove
from PIL import Image
from .models import Rembg
from prof.models import Profile
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
import os



# Create your views here.
#REMBG SECTION-----------------------------------------------------------------------------------------

def tools_index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()

    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
    }
    return render(request, 'tools/tools_index.html', context)

def tools_rembg(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    new_pic = Rembg.objects.all().filter(user=user_profile)
    if request.method == "POST":
        image = request.FILES.get('image')
        im = image.name
        input = Image.open(image)
        output_path = os.path.splitext(im)[0] + '.png'
        output = remove(input)
        output.save('media/'+output_path)
        s = Rembg.objects.create(user=user_profile, output=output_path)
        s.save()
        return redirect('/tools-rembg')
    
        
    
    context = {
        'pics' : new_pic,
        'user_profile':user_profile,
        'all_user' : all_user,
    }
    return render(request, 'tools/tools_rembg.html', context)


def delete_rembg(request, pk):
    item = Rembg.objects.get(id=pk)
    pics = item.output
    fs = FileSystemStorage()
    fs.delete(pics.name)
    item.delete()
    return redirect('tools-rembg')

#-------------------------------------------------------------------------------------------------------
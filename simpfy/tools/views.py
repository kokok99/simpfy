from django.shortcuts import render, redirect
from rembg import remove
from PIL import Image
from .models import Rembg, Ytvidmp, Yt, Word
from prof.models import Profile
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from pytube import YouTube
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from docx2pdf import convert
import pythoncom
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
        if image:
            im = image.name
            input = Image.open(image)
            output_path = os.path.splitext(im)[0] + '.png'
            output = remove(input)
            output.save('media/'+output_path)
            s = Rembg.objects.create(user=user_profile, output=output_path)
            s.save()
            return redirect('/tools-rembg')
        else:
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

#---------------------------------YOUTUBE TO MP3--------------------------------------------------------
def yt2mp3(request) :
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    new_file = Ytvidmp.objects.all().filter(user=user_profile)
    if request.method == "POST":
        url = request.POST['url']
        if url:
            yt = YouTube(str(url))
            video = yt.streams.filter(only_audio=True).first()
            output = video.download(output_path='media/')
            base, ext = os.path.splitext(output)
            newf = base + '.mp3'
            os.rename(output, newf)
            s = Ytvidmp.objects.create(user = user_profile, output=newf)
            s.save()
            return redirect('/ytvid')
        else:
            return redirect('/ytvid')
    
    context = {
        'new_file' : new_file,
        'user_profile':user_profile,
        'all_user' : all_user,
    }

    return render(request, 'tools/tools_ytvidtomp3.html', context)

def delmp3(request):
    if request.method == "POST":
        id = request.POST['id']
        mp3 = Ytvidmp.objects.get(id=id)
        output = mp3.output
        fs = FileSystemStorage()
        file_path = output.name
        wrapper = FileWrapper(open(file_path, 'rb'))
        response = HttpResponse(wrapper, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename=' + file_path
        fs.delete(output.name)
        mp3.delete()
        return response

#-------------------------------------------------------------------------------------------------------

#-------------------------------YOUTUBE VIDEO DOWNLOAD------------------------------------------------

def yt(request) :
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    new_file = Yt.objects.all().filter(user=user_profile)
    if request.method == "POST":
        url = request.POST['url']
        if url:
            yt = YouTube(str(url))
            video = yt.streams.get_highest_resolution()
            output = video.download(output_path='media/')
            base, ext = os.path.splitext(output)
            newf = base + '.mp4'
            os.rename(output, newf)
            s = Yt.objects.create(user = user_profile, output=newf)
            s.save()
            return redirect('/yt')
        else:
            return redirect('/yt')
    
    context = {
        'new_file' : new_file,
        'user_profile':user_profile,
        'all_user' : all_user,
    }

    return render(request, 'tools/tools_yt.html', context)

def delyt(request):
    if request.method == "POST":
        id = request.POST['id']
        mp3 = Yt.objects.get(id=id)
        output = mp3.output
        fs = FileSystemStorage()
        file_path = output.name
        wrapper = FileWrapper(open(file_path, 'rb'))
        response = HttpResponse(wrapper, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename=' + file_path
        fs.delete(output.name)
        mp3.delete()
        return response
#-----------------------------------------------------------------------------------------------------

#------------------------------------IMAGE TO PDF-----------------------------------------------------
def word2pdf(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    new_file = Word.objects.all().filter(user=user_profile)
    if request.method == "POST":
        word = request.FILES.get('word')
        if word:
            w = Word.objects.create(user=user_profile, input=word)
            w.save()
            fe = Word.objects.get(user=user_profile)
            words = fe.input
            inword = words.name
            pythoncom.CoInitialize()
            convert(inword)
            convert("media/")

            wrd = word.name
            output_path = os.path.splitext(wrd)[0] + '.pdf'
            wd = Word.objects.create(user=user_profile, output=output_path)
            wd.save()
            return redirect('/word2pdf')
        else:
            return redirect('/word2pdf')
    
    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'new_file' : new_file,
    }

    return render(request, 'tools/word2pdf.html', context)
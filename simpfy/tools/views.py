from django.shortcuts import render, redirect
from prof.models import Profile
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Wolf, Wiki, Wikihow, Wolfmath, Wolfweather, Qr, Bar, Hist, Line, Scatter, Line2, Xcel2csv,  Mp324
import wolframalpha
import wikipedia
import pyqrcode
from whapi import search, get_html, get_images, parse_steps
from django.contrib import messages
from PIL import Image
from django.core.files.storage import FileSystemStorage
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import moviepy
import moviepy.editor
import png
import os



# Create your views here.
#INDEX SECTION-----------------------------------------------------------------------------------------

def tools_index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)

    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
    }
    return render(request, 'tools/tools_index.html', context)

#----------------------------WOLFRAMALPHA-----------------------------------------------------------------
def wolf(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Wolf.objects.all().filter(user=user_profile)
    if request.method == "POST":
        quest = request.POST['ask']
        if quest:
            app_id = "HT4JHK-U642Y56XLE"
            client = wolframalpha.Client(app_id)
            res = client.query(quest)
            for pod in res.results:
                for sub in pod.subpods:
                    an = sub.img
            tx = next(res.results).text
            img = an['@src']
            
            ansimg = img
            anstext = tx
            s = Wolf.objects.create(user=user_profile,quest=quest, outputtext=anstext, outputimg=ansimg)
            s.save()  
            return redirect('/wolf')
        else:
            return redirect('/wolf')

    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
    }
    return render(request, 'tools/tools_wolf.html', context)

def wolfmath(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Wolfmath.objects.all().filter(user=user_profile)
    if request.method == "POST":
        quest = request.POST['ask']
        if quest:
            app_id = "HT4JHK-U642Y56XLE"
            client = wolframalpha.Client(app_id)
            res = client.query(quest)
            for pod in res.results:
                for sub in pod.subpods:
                    an = sub.img
            tx = next(res.results).text
            img = an['@src']
            
            ansimg = img
            anstext = tx
            s = Wolfmath.objects.create(user=user_profile,quest=quest, outputtext=anstext, outputimg=ansimg)
            s.save()  
            return redirect('/wolfmath')
        else:
            return redirect('/wolfmath')

    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
    }
    return render(request, 'tools/tools_wolfmath.html', context)

def wolfweather(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Wolfweather.objects.all().filter(user=user_profile)
    if request.method == "POST":
        quest = request.POST['ask']
        if quest:
            app_id = "HT4JHK-U642Y56XLE"
            client = wolframalpha.Client(app_id)
            res = client.query(quest)
            for pod in res.results:
                for sub in pod.subpods:
                    an = sub.img
            tx = next(res.results).text
            img = an['@src']
            
            ansimg = img
            anstext = tx
            s = Wolfweather.objects.create(user=user_profile,quest=quest, outputtext=anstext, outputimg=ansimg)
            s.save()  
            return redirect('/wolfweather')
        else:
            return redirect('/wolfweather')

    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
    }
    return render(request, 'tools/tools_wolfweather.html', context)

def wolfdel(request, pk):
    q = Wolf.objects.get(id=pk)
    q.delete()
    messages.info(request, "Successfully deleted ")
    return redirect('/wolf')

def wolfweatherdel(request, pk):
    q = Wolfweather.objects.get(id=pk)
    q.delete()
    messages.info(request, "Successfully deleted ")
    return redirect('/wolfweather')

def wolfmathdel(request, pk):
    q = Wolfmath.objects.get(id=pk)
    q.delete()
    messages.info(request, "Successfully deleted ")
    return redirect('/wolfmath')
#------------------------------------------------------------------------------------------------------------

#--------------------------------------WIKIPEDIA----------------------------------------------------------

def wiki(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Wiki.objects.all().filter(user=user_profile)

    if request.method == "POST":
        quest = request.POST['ask']
        if quest:
            ans = wikipedia.summary(quest, sentences=5)
            s = Wiki.objects.create(user=user_profile, quest=quest, outputtext=ans)
            s.save()
            messages.info(request, "Good Search!")
            return redirect('/wiki')
        else:
            messages.info(request, "No Input From You :(")
            return redirect('/wiki')


    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
    }
    return render(request, 'tools/tools_wiki.html', context)

def wikidel(request, pk):
    q = Wiki.objects.get(id=pk)
    q.delete()
    messages.info(request, "successfully deleted !")
    return redirect('/wiki')

#--------------------------------------------------------------------------------------------------------

#-----------------------------------------WIKIHOW----------------------------------------------------------------

def wikihow(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Wikihow.objects.all().filter(user=user_profile)

    if request.method == "POST":
        q = request.POST['ask']
        if q:
            q_res = search(q, 4)
            for quest in q_res:
                title = quest['title']
                id_title = quest['article_id']
                s = Wikihow.objects.create(user=user_profile, quest=q, title=title, id_title=id_title)
                s.save()
            messages.info(request, "Your results is down below!")
            return redirect('/wikihow')
        else:
            messages.info(request, "No Input :(")
            return redirect('/wikihow')
    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
        
    }
    return render(request, 'tools/tools_wikihow.html', context)

def wikihowres(request, pk):
    res = Wikihow.objects.get(id_title=pk)
    ht = res.html

    context = {
        'res' : ht
    }
    return render(request, 'tools/tools_wikihowres.html', context)

def wikihowdel(request, pk):
    q = Wikihow.objects.get(id=pk)
    q.delete()
    messages.info(request, "successfully deleted !")
    return redirect('/wikihow')
#---------------------------------------------------------------------------------------------------------------

#---------------------------------------LINK TO QR CODE--------------------------------------------------------

def qr(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Qr.objects.all().filter(user=user_profile)
    if request.method == "POST":
        q = request.POST['qr']
        if q:
            user = request.user.username
            output_path =  user+"Qr.png"
            fs = FileSystemStorage()
            fs.delete("media/"+output_path)
            de = Qr.objects.all()
            de.delete()
            qr_code = pyqrcode.create(q)
            qr_code.png("media/"+output_path, scale=7)
            s = Qr.objects.create(user=user_profile, qr=q, res=output_path)
            s.save()
            messages.success(request, 'Done !')
            return redirect('/qr')
        else :
            messages.info(request, 'No Input  !')
            return redirect('/qr')


    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
        
    }
    return render(request, 'tools/tools_qr.html', context)

def delqr(request, pk):
    qr = Qr.objects.get(id=pk)
    fs = FileSystemStorage()
    output = qr.res.name
    fs.delete(output)
    qr.delete()
    return redirect('/qr')


#--------------------------------------------------------------------------------------------------------------

#------------------------------DATA VISUALIZATION------------------------------------------------------------
def bar(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Bar.objects.all().filter(user=user_profile)

    if request.method == "POST":
        file = request.FILES['file']
        x = request.POST['x']
        y = request.POST['y']
        ind = request.POST['ind']
        if file:
            user = request.user.username
            input = file.name
            output = user+'Bar.png'
            fs = FileSystemStorage()
            fs.delete("media/"+output)
            de = Bar.objects.all()
            de.delete()
            data = pd.read_csv(file)
            sns.barplot(x=x, y=y, data=data, hue=ind)
            plt.savefig("media/"+output)
            s = Bar.objects.create(user=user_profile, file=output)
            s.save()
            messages.info(request, 'Success visualizing you data !')
            return redirect('/bar')
        else:
            messages.info(request, 'No File :(')
            return redirect('/bar')


    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
        
    }

    return render(request, 'tools/tools_bar.html', context)

def hist(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Hist.objects.all().filter(user=user_profile)

    if request.method == "POST":
        file = request.FILES['file']
        x = request.POST['x']
        ind = request.POST['ind']
        if file:
            user = request.user.username
            input = file.name
            output = user+'Hist.png'
            fs = FileSystemStorage()
            fs.delete("media/"+output)
            de = Hist.objects.all()
            de.delete()
            data = pd.read_csv(file)
            sns.histplot(x=x,data=data, hue=ind)
            plt.savefig("media/"+output)
            s = Hist.objects.create(user=user_profile, file=output)
            s.save()
            messages.info(request, 'Success visualizing you data !')
            return redirect('/hist')
        else:
            messages.info(request, 'No File :(')
            return redirect('/hist')


    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
        
    }

    return render(request, 'tools/tools_hist.html', context)


def line(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Line.objects.all().filter(user=user_profile)

    if request.method == "POST":
        file = request.FILES['file']
        x = request.POST['x']
        y = request.POST['y']
        if file:
            user = request.user.username
            input = file.name
            output = user+'Line.png'
            fs = FileSystemStorage()
            fs.delete("media/"+output)
            de = Line.objects.all()
            de.delete()
            data = pd.read_csv(file)
            sns.lineplot(x=x, y=y, data=data)
            plt.savefig("media/"+output)
            s = Line.objects.create(user=user_profile, file=output)
            s.save()
            messages.info(request, 'Success visualizing you data !')
            return redirect('/line')
        else:
            messages.info(request, 'No File :(')
            return redirect('/line')


    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
        
    }

    return render(request, 'tools/tools_line.html', context)

def scatter(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Scatter.objects.all().filter(user=user_profile)

    if request.method == "POST":
        file = request.FILES['file']
        x = request.POST['x']
        y = request.POST['y']
        ind = request.POST['ind']
        if file:
            user = request.user.username
            input = file.name
            output = user+'Scatter.png'
            fs = FileSystemStorage()
            fs.delete("media/"+output)
            de = Scatter.objects.all()
            de.delete()
            data = pd.read_csv(file)
            sns.scatterplot(x=x, y=y, data=data, hue=ind)
            plt.savefig("media/"+output)
            s = Scatter.objects.create(user=user_profile, file=output)
            s.save()
            messages.info(request, 'Success visualizing you data !')
            return redirect('/scatter')
        else:
            messages.info(request, 'No File :(')
            return redirect('/scatter')


    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
        
    }

    return render(request, 'tools/tools_scatter.html', context)

def line2(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Line2.objects.all().filter(user=user_profile)

    if request.method == "POST":
        file = request.FILES['file']
        drop = request.POST['drop']

        if file:
            user = request.user.username
            input = file.name
            output = user+'Line2.png'
            fs = FileSystemStorage()
            fs.delete("media/"+output)
            de = Line2.objects.all()
            de.delete()
            data = pd.read_csv(file)
            sns.lineplot(data=data.drop([drop], axis=1))
            plt.savefig("media/"+output)
            s = Line2.objects.create(user=user_profile, file=output)
            s.save()
            messages.info(request, 'Success visualizing you data !')
            return redirect('/line2')
        else:
            messages.info(request, 'No File :(')
            return redirect('/line2')


    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
        
    }

    return render(request, 'tools/tools_line2.html', context)

#-----------------------------------------------------------------------------------------------------------

#--------------------------------------EXCEL TO CSV----------------------------------------------------------

def xcel2csv(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Xcel2csv.objects.all().filter(user=user_profile)

    if request.method == "POST":
        xcel = request.FILES['xcel']
        if xcel:
            user = request.user.username
            input = xcel.name
            output = user+'Result.csv'
            fs = FileSystemStorage()
            fs.delete("media/"+output)
            de = Xcel2csv.objects.all()
            de.delete()
            read_file = pd.read_excel(xcel)
            read_file.to_csv("media/"+output)
            s = Xcel2csv.objects.create(user=user_profile, file=output)
            s.save()
            messages.info(request, 'Convert Done !')
            return redirect('/xcel2csv')
        else:
            messages.info(request, 'No Files :(')
            return redirect('/xcel2csv')

    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
        
    }

    return render(request, 'tools/tools_xcel2csv.html', context)

#------------------------------------------------------------------------------------------------------------

#----------------------------------------mp4 to mp3-------------------------------------------------------

def mp324(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    user_request = User.objects.get(username=request.user.username)
    user_req = Profile.objects.get(user=user_request)
    answer = Mp324.objects.all().filter(user=user_profile)

    if request.method == "POST":
        vid = request.FILES['file']
        if vid:
            user = request.user.username
            input = vid.name
            output = user+"Res.mp3"
            fs = FileSystemStorage()
            fs.delete("media/"+output)
            de = Mp324.objects.all()
            de.delete()
            fs.save(input, vid)
            video = moviepy.editor.VideoFileClip("media/"+input)
            audio = video.audio
            audio.write_audiofile("media/"+output)
            s = Mp324.objects.create(user=user_profile, file=output)
            s.save()
            video.close()
            fs.delete(input)
            messages.info(request, "video successfully converted!")
            return redirect("/mp324")
        else:
            messages.info(request, "No input :(")
            return redirect("/mp324")



    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'user_req' : user_req,
        'answer' : answer
        
    }

    return render(request, 'tools/tools_mp324.html', context)


#---------------------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect
from prof.models import Profile
from django.contrib.auth.models import User, auth
from .models import Wolf, Wiki, Wikihow, Wolfmath, Wolfweather
import wolframalpha
import wikipedia
from whapi import search, get_html, get_images, parse_steps
from django.contrib import messages
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

#---------------------------------------------------------------------------------------------------------------
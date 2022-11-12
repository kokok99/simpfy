from django.shortcuts import render, redirect
from prof.models import Profile
from django.contrib.auth.models import User, auth
from .models import Wolf
import wolframalpha
import os



# Create your views here.
#INDEX SECTION-----------------------------------------------------------------------------------------

def tools_index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()

    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
    }
    return render(request, 'tools/tools_index.html', context)

#----------------------------WOLFRAMALPHA-----------------------------------------------------------------
def wolf(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_user = Profile.objects.all()
    answer = Wolf.objects.all().filter(user=user_profile)
    if request.method == "POST":
        quest = request.POST['ask']
        if quest:
            app_id = "HT4JHK-U642Y56XLE"
            client = wolframalpha.Client(app_id)
            res = client.query(quest)
            ans = next(res.results).text
            s = Wolf.objects.create(user=user_profile,quest=quest, output=ans)
            s.save()  
            return redirect('/wolf')
        else:
            return redirect('/wolf')

    context = {
        'user_profile':user_profile,
        'all_user' : all_user,
        'answer' : answer
    }
    return render(request, 'tools/tools_wolf.html', context)

def wolfdel(request, pk):
    q = Wolf.objects.get(id=pk)
    q.delete()
    return redirect('/wolf')

#------------------------------------------------------------------------------------------------------------
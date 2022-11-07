from django.shortcuts import render, redirect
from rembg import remove
from PIL import Image
from .models import Rembg

# Create your views here.
def tools_index(request):
    return render(request, 'tools/tools_index.html')

def tools_rembg(request):
    pics = Rembg.objects.all()
    if request.method == "POST":
        image = request.POST['image']
        insert = Rembg.objects.create(image=image)
        insert.save()
        input = Image.open(insert)
        output = remove(input)
        save = output.save('output.png')
        rem = Rembg.objects.create(output=save)
        rem.save()
        return redirect('/tools-rembg')
    
    context = {
        'pics' : pics
    }
    return render(request, 'tools/tools_rembg.html', context)
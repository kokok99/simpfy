from django.shortcuts import render, redirect
from rembg import remove
from PIL import Image
from .models import Rembg
from django.core.files.storage import FileSystemStorage


# Create your views here.
def tools_index(request):
    return render(request, 'tools/tools_index.html')

def tools_rembg(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        input = Image.open(image)
        output = remove(input)
        output.save('media/rembg/output.png')
        return redirect('/tools-rembg')
    fs = FileSystemStorage()
    new_pic = fs.generate_filename('media/rembg/output.png')
        
    
    context = {
        'pics' : new_pic
    }
    return render(request, 'tools/tools_rembg.html', context)
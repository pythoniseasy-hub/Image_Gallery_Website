from django.shortcuts import render,redirect
from MyGalleryApp.models import ImageGallery
# Create your views here.
def index(request):
    images = ImageGallery.objects.all()
    return render(request,"index.html",{'images':images})

def handle_upload(request):
    new_shrdimg = ImageGallery()
    new_shrdimg.image = request.FILES['file']
    new_shrdimg.title = request.POST['title']
    new_shrdimg.description = request.POST['description']
    new_shrdimg.save()
    return redirect("main")
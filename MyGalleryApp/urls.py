from django.urls import path
from MyGalleryApp import views

urlpatterns = [
    path('',views.index,name="main"),
    path('upload',views.handle_upload,name="upload"),
]

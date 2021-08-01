from django.shortcuts import render
from .models import Post
#create your views here.
def newapp_list(request):
    post=Post.objects.all()
    context={
        'newapp_list':post
    }
    return render(request,"newapp/newapp_list.html",context)
# Create your views here.

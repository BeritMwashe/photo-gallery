from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def home(request):
    post=Post.objects.filter(owner=request.user.id)
    
    return render(request,'home/index.html',{'post':post, 'name':'berit'})


def singlepost(request,post_id):
    post=Post.objects.get(id=post_id)
    return render(request,'home/single_post',{'post':post})
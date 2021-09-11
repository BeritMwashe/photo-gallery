from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def home(request):
    post=Post.objects.all()
    print(post)
    print(request.user.employee.profile_img)
    return render(request,'home/index.html',{'post':post, 'name':'berit'})



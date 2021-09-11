from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect


# Create your views here.
def home(request):
    print(request.user.employee.profile_img)
    return render(request,'home/index.html')


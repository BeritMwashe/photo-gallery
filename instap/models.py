from django.contrib.auth.models import User
from django.db import models
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='profile_pic/')
    


class Post(models.Model):
    userpost=models.ImageField(upload_to='posts')
    description=models.CharField(max_length=1000)
    title=models.CharField(max_length=50)
    pub_date=models.DateTimeField()
    


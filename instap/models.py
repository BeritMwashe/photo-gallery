from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

# class Followers(models.Model):
#     name=models.CharField(max_length=100)
#     user_id=models.IntegerField()

class Followers(models.Model):
    uname=models.CharField(max_length=100)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    # user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    # follower_uname=models.TextField(max_length=100)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='profile_pic/')
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='profile_pic/')
   


class Post(models.Model):

    userpost=models.ImageField(upload_to='posts')
    caption=models.CharField(max_length=1000)
    pub_date=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def delete_image(cls,id):
        objToDel=cls.objects.get(id=id).delete()
    @classmethod
    def update_caption(cls):
        cls.update_image()
    @classmethod
    def save_image(cls,id):
        cls.save()


class LikeClass(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)



class DisLiked(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)


class commets(models.Model):
    title=models.CharField(max_length=100)
    comment=HTMLField()
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    



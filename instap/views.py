import os
from instap.forms import CommentForm, PostForm, UpdateCaptionForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Followers, Post,LikeClass,DisLiked, commets
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def allu(request):
    allusers=User.objects.all()
    return render(request,'home/timelineimages.html',{'users':allusers})
@login_required(login_url='/accounts/login/')
def home(request):
    
    allusers=User.objects.all()
    user=User.objects.get(id=request.user.id)
    post=Post.objects.filter(owner=request.user.id)
    print(post)
    followers=Followers.objects.filter(uname=request.user.username)
    print(followers)
    followings=Followers.objects.filter(user_id=request.user.id)
    print(followings)
    ar=[]
    for post in post:
        followings=Followers.objects.filter(user_id=request.user.id)
        followers=Followers.objects.filter(uname=request.user.username)
    # print(followers)
        for followers in followers:
            if post.owner.id==followers.id:
                ar.append(post)
        
        for followers in followings:
            if post.owner.id==followers.id:
                ar.append(post)
        if post.owner.id==request.user.id:
            ar.append(post)
    print(ar)

    # return HttpResponse('hello')
   
    # for f in followings:
    #     print(f.uname)
    return render(request,'home/timelineimages.html',{'post':ar, 'name':'berit','users':allusers,'user':user,'followers':followers,'following':followings})

@login_required(login_url='/accounts/login/')
def singlepost(request,post_id):
    likes=LikeClass.objects.filter(post_id=post_id)
    dislikes=DisLiked.objects.filter(post_id=post_id)
    post=Post.objects.get(id=post_id)
    comments=commets.objects.filter(post_id=post_id)
    return render(request,'home/singlepost.html',{'post':post,'likes':likes,'dislikes':dislikes,'comments':comments})



@login_required(login_url='/accounts/login/')
def followU(request,id):
    userTobefollowed=User.objects.get(id=id)
    currentUser=User.objects.get(id=request.user.id)
    print(currentUser.id)
    print(userTobefollowed.id)
 
 
    if userTobefollowed.id ==currentUser.id:
            messages.add_message(request,messages.INFO,'{0} you cant follow yourself.'.format(request.user))
            # folowerToremove=Followers(name=request.user.username,user_id=userTobefollowed.id,follower_id=request.user.url)
            # folowerToremove.remove(currentUser)
    else:
            print('no')
            folowerToadd=Followers(uname=currentUser.username,user_id=userTobefollowed)
            print(folowerToadd)
            folowerToadd.save()
    return redirect('/')
@login_required(login_url='/accounts/login/')
def Like(request,post_id):
 
    postTobeliked=Post.objects.get(id=post_id)
    currentUser=User.objects.get(id=request.user.id)
    postowner=User.objects.get(id=postTobeliked.owner_id)
    print(currentUser)
    likes=LikeClass.objects.all()
    likeToadd=LikeClass(user_id=currentUser,post_id=postTobeliked)
    
    if postowner.id ==currentUser.id :
            print('yer')
            # alert('cant like own picture')
            # folowerToremove=Followers(name=request.user.username,user_id=userTobefollowed.id,follower_id=request.user.url)
            # folowerToremove.remove(currentUser)
    else:   
            print('no')
            # likeToadd=LikeClass(user_id=currentUser,post_id=postTobeliked)
            print(likeToadd)
            likeToadd.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))







@login_required(login_url='/accounts/login/')
def DisLike(request,post_id):
 
    postTobeliked=Post.objects.get(id=post_id)
    currentUser=User.objects.get(id=request.user.id)
    postowner=User.objects.get(id=postTobeliked.owner_id)
    print(currentUser)
    likes=DisLiked.objects.all()
    likeToadd=DisLiked(user_id=currentUser,post_id=postTobeliked)
    
    if postowner.id ==currentUser.id :
            print('yer')
            # alert('cant like own picture')
            # folowerToremove=Followers(name=request.user.username,user_id=userTobefollowed.id,follower_id=request.user.url)
            # folowerToremove.remove(currentUser)
    else:   
            print('no')
            # likeToadd=LikeClass(user_id=currentUser,post_id=postTobeliked)
            print(likeToadd)
            likeToadd.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def addpost(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # article = form.save(commit=False)
            # article.owner = current_user
            # article.save()
            article=form.save(commit=False)
            article.owner=current_user
            article.save()
        return redirect('/')

    else:
        form = PostForm()
    return render(request, 'home/new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def addcomment(request,post_id):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            post=Post.objects.get(id=post_id)
            comment = form.save(commit=False)
            comment.user_id= current_user
            comment.post_id=post
            comment.save()
        return redirect('/')

    else:
        form = CommentForm()
    return render(request, 'home/new_comment.html', {"form": form,'post_id':post_id
    })

@login_required(login_url='/accounts/login/')
def search_results(request):
   
    if 'people' in request.GET and request.GET["people"]:
        search_term = request.GET.get("people")
        searched_articles = User.objects.filter(username__contains=search_term)
        message = f"{search_term}"
        arr=[]
        for searched_articles in searched_articles:
            searched_articles=User.objects.get(id=searched_articles.id)
            arr.append(searched_articles)


        return render(request, 'home/search.html',{"message":message,"user": arr})

    else:
        message = "You haven't searched for any term"
        return render(request, 'home/search.html',{"message":message})
@login_required(login_url='/accounts/login/')
def oneuser(request,id):
    allusers=User.objects.all()
    post=Post.objects.filter(owner=id)
    user=User.objects.get(id=id)
    followers=Followers.objects.filter(uname=user.username)
    # print(followers)
    followings=Followers.objects.filter(user_id_id=user.id)
   
    # for f in followings:
    #     print(f.uname)
    return render(request,'home/index.html',{'followers':followers,'following':followings,'post':post, 'users':allusers,'user':user})
@login_required(login_url='/accounts/login/')
def delete_img(request,id):
    objToDel=Post.objects.get(id=id)
    if objToDel.owner.id ==request.user.id:
        delGal=Post.delete_image(id=id)
        os.remove(objToDel.userpost.path)
        
        return redirect('/')
@login_required(login_url='/accounts/login/')
def update_caption(request,post_id):
    post=Post.objects.get(id=post_id)
    if post.owner.id ==request.user.id:
        return render(request, 'home/updatecap_post.html',{'post_id':post_id})
@login_required(login_url='/accounts/login/')
def edit_caption(request,post_id):
    post=Post.objects.get(id=post_id)
    if post.owner.id ==request.user.id:
        if 'caption' in request.GET and request.GET["caption"]:
            search_term = request.GET.get("caption")
            Post.objects.filter(id=post_id).update(caption=search_term)
        return redirect('/')



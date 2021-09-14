from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls.conf import path
from . import views


urlpatterns=[
    url(r'^$',views.home,name='indexpage'),
    # url('allu/(\d+)', views.allu, name='getallfollowers'),
    url(r'^singlepost/(\d+)',views.singlepost,name='singlepost'),
    url(r'^like/(\d+)',views.Like,name='like'),
    url(r'^dislike/(\d+)',views.DisLike,name='dislike'),
    url('followU/(\d+)',views.followU,name='followU'),
    url(r'^addpost',views.addpost,name='addpost'),
    url(r'^addcomment/(\d+)',views.addcomment,name='addcomment'),
    url(r'^search/', views.search_results, name='search_results'),
    url('oneuser/(\d+)', views.oneuser, name='oneuser'),
    url('updatecap/(\d+)', views.update_caption, name='updatecap'),
    url('updatecaption/(\d+)', views.edit_caption, name='updatecaption'),
    url(r'^deleteimage/(\d+)',views.delete_img,name='deleteimg')]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
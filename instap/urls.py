from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls.conf import path
from . import views


urlpatterns=[
    url(r'^$',views.home,name='indexpage'),
    url(r'^$',views.singlepost,name='singlepost'),]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
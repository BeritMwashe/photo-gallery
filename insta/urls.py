"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from instap.forms import MyCustomUserForm
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from django_registration.backends.one_step.views import RegistrationView
from django.conf.urls import include
urlpatterns = [
    # path('accounts/register/',
    #     RegistrationView.as_view(
    #         form_class=MyCustomUserForm
    #     ),
    #     name='django_registration_register',
    # ),
    url('accounts/register/',
        RegistrationView.as_view(success_url='/accounts/login'),
        name='django_registration_register'),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    
    path('', include('instap.urls')),
]

"""prakriti URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =  [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('terms/', views.terms, name='terms'), 
    path('demo/', views.demo, name='demo') ,
    path('services/', views.services, name='services'), 
    path('voicebot/', views.voicebot, name='voicebot') ,
    path('textbot/', views.textbot, name='textbot') ,
    path('virtualbuddy/', views.virtualbuddy, name='virtualbuddy'),
    path('socialmediabot/', views.socialmediabot, name='socialmediabot'),
    path('newsbot/', views.newsbot, name='newsbot'),
    path('telegrambot/', views.telegrambot, name='telegrambot'),
    path('whatsappbot/', views.whatsappbot, name='whatsappbot'),
    path('emailbot/', views.emailbot, name='emailbot'),
    path('smsbot/', views.smsbot, name='smsbot'),

 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

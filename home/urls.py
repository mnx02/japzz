from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("", views.register, name='home'),
    path("about.html", views.about, name='about.html'),
    path("login.html", views.login, name='login.html'),
    path("index.html", views.index, name='index.html'),
    path("Change_password.html", views.userchangepassword, name='Change_password.html'),
    path("Close_account.html", views.closeaccount, name='Close_account'),
    path("Videochat.html", views.videochat, name='Videochat.html'),
    path("worldchat.html", views.worldchat, name='worldchat.html'),
    path("user-notification.html", views.usernotification, name='user-notification.html'),
    path("user-setting.html", views.settings, name='user-setting.html'),
    path("Verify.html", views.verifyaccount, name='Verify.html'),
    path("contact.html", views.contact, name='contact.html'),
    
    
]
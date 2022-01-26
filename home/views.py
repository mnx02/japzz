from django.shortcuts import render



from home.models import Register
from django.contrib import messages

def register(request):
    if request.method == "POST":
         username = request.POST.get('username')
         email = request.POST.get('email')
         password = request.POST.get('password')
         confirmpassword = request.POST.get('confirmpassword')
         name = request.POST.get('name')
         dob = request.POST.get('dob')
         gender = request.POST.get('gender')
         city = request.POST.get('city')
         register = Register(username=username, email=email, password=password, confirmpassword=confirmpassword, name=name, dob=dob, gender=gender,  city=city)
         register.save()
         messages.success(request, 'Your message has been sent!')
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')
def index(request):
    return render(request, 'index.html')
def userchangepassword(request):
    return render(request, 'Change_password.html')
def closeaccount(request):
    return render(request, 'Close_account.html')
def videochat(request):
    return render(request, 'Videochat.html')
def worldchat(request):
    return render(request, 'worldchat.html')
def usernotification(request):
    return render(request, 'user-notification.html')
def settings(request):
    return render(request, 'user-setting.html')
def verifyaccount(request):
    return render(request, 'user-verify-account.html')
def contact(request):
    return render(request, 'contact.html')

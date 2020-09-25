from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
import random

def home(request):
    projects=Project.objects.all()
    return render(request,"portfolio/home.html",{"projects":projects})

def aboutus(request):
    projects=Project.objects.all()
    return render(request,"portfolio/aboutus.html",{"projects":projects})

#Password_generator
def home1(request):
    return render(request,"portfolio/password_generator/home.html")

def aboutus1(request):
    return render(request,"portfolio/password_generator/aboutus.html")

def password(request):
    characters=list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("special"):
        characters.extend(list("!#$%&()=~|{`}*+_?><,./\]:;[@]`}"))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    length=int(request.GET.get("length",12))
    thepassword=""
    for x in range(length):
        thepassword=thepassword+random.choice(characters)
    return render(request,"portfolio/password_generator/password.html",{"password":thepassword})

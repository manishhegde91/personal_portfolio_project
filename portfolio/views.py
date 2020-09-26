from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Todo
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError, OperationalError
from django.contrib.auth import login,logout, authenticate
from .forms import TodoForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
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


    #todo

def home2(request):
    return render(request,'portfolio/todo/home.html')

def signupuser(request):
    #For filling the form
    if request.method=="GET":
        #UserCreationForm is a django function to create forms
        return render(request,'portfolio/todo/signupuser.html',{'form':UserCreationForm()})
    else:
        #Validating both the passwords are correct
        if request.POST['password1']==request.POST['password2']:
            #Create a new form(After clicking on submit button)
            try:
                #Creating username and password
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                #Registering username and password
                user.save()
                login(request,user)
                #Redirect to current todos page
                return redirect('currenttodos')

            #Username already exists
            except IntegrityError:
                return render(request,'portfolio/todo/signupuser.html',{'form':UserCreationForm(), 'error':'Username already exists.'})
        else:
            return render(request,'portfolio/todo/signupuser.html',{'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method=="GET":
        #AuthenticationForm is a django function to login
        return render(request,'portfolio/todo/login.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'portfolio/todo/login.html',{'form':AuthenticationForm(), 'error':'Username and Password did not match'})
        else:
            login(request,user)
            return redirect('currenttodos')

@login_required
def logoutuser(request):
    #POST request is to logout.
    if request.method == 'POST':
        logout(request)
        return redirect('home2')

@login_required
def createtodos(request):
    if request.method=="GET":
        return render(request,'portfolio/todo/createtodo.html',{'form':TodoForm()})
    else:
        try:
            #To save the todo list in the admin page after clicking on create button
            form = TodoForm(request.POST)
            newtodo=form.save(commit=False)
            newtodo.user=request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request,'portfolio/todo/createtodo.html',{'form':TodoForm(),'error':'Bad data passed in, Please try again....'})

@login_required
def currenttodos(request):
    #Displaying todos on the front page as per the user
    todos=Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request,'portfolio/todo/currenttodos.html',{'todos':todos})

@login_required
def viewtodo(request, todo_pk):
    todo=get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=="GET":
        form = TodoForm(instance=todo)
        return render(request,'portfolio/todo/viewtodo.html',{'todo':todo,'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request,'portfolio/todo/viewtodo.html',{'todo':todo,'form':form, 'error':'Bad data'})

@login_required
def completetodo(request, todo_pk):
    todo=get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=="POST":
        todo.datecompleted=timezone.now()
        todo.save()
        return redirect('currenttodos')

@login_required
def deletetodo(request, todo_pk):
    todo=get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=="POST":
        todo.delete()
        return redirect('currenttodos')

@login_required
def completedtodos(request):
    #Displaying todos on the front page as per the user
    todos=Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request,'portfolio/todo/completedtodos.html',{'todos':todos})

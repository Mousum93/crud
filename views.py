from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if request.method == 'POST':
        data = request.POST 
        fname=data.get('fname')
        lname=data.get('lname')
        uname=data.get('uname')
        password=data.get('password')

        if User.objects.filter(username=uname).exists():
            return render(request,"index.html",{"error":"invalid input"})
        u=User(first_name=fname,last_name=lname,username=uname)
        u.set_password(password)
        u.save()

        return render(request,"index.html",{"msg":"registrationdone"})
    
    return render(request,"index.html") 

def log(request):
    if request.method == 'POST':
        data = request.POST 
        uname=data.get('uname')
        password=data.get('password')

        u=authenticate(username=uname,password=password)
        if u is None:
            return render(request,"index.html",{"error":"invalid input"})
        else:
            login(request,u)
            return redirect("home")
    
    return render(request,"log.html")
    
@login_required(login_url='logpage')
def home(request):
    return render(request,"home.html")
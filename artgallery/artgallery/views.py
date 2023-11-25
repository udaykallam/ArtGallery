from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from adminapp.models import Admin
from django.db.models import Q
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from adminapp.models import Product
from artistapp.models import Artist

def homefunction(request):
    products = Product.objects.all()
    return render(request,"customerapp/index.html",{'products': products})

def aboutfunction(request):
    return render(request,"customerapp/about.html")

def loginfunction(request):
    return render(request,"login.html")

def aboutfunction(request):
    return render(request,"customerapp/about.html")

def homefunction(request):
    products = Product.objects.all()
    return render(request,"customerapp/home.html",{'products':products})

def loginPage(request):
    return render(request,'login.html')

def signupfunction(request):
    if request.method == 'POST':
        adminuname = request.POST.get('user')
        adminemail = request.POST.get('email')
        adminpwd = request.POST.get('pass1')
        adminpwd2 = request.POST.get('pass2')
        try:
            validate_email(adminemail)
        except ValidationError:
            message = "Invalid email address."
            return render(request,'signup.html', {"message": message})
        if User.objects.filter(username=adminuname).exists():
            message = "An account with this username already exists."
            return render(request,'signup.html', {"message": message})
        if adminpwd != adminpwd2:
            message = "Passwords don't match!!"
            return render(request,'signup.html', {"message": message})
        elif len(adminpwd) < 8:
            message = "Password must be at least 8 characters long."
            return render(request,'signup.html', {"message": message})
        elif not re.search(r'[A-Z]', adminpwd):
            message = "Password must contain at least one uppercase letter."
            return render(request, 'signup.html', {"message": message})
        elif not re.search(r'[a-z]', adminpwd):
            message = "Password must contain at least one lowercase letter."
            return render(request, 'signup.html', {"message": message})
        elif not re.search(r'[0-9]', adminpwd):
            message = "Password must contain at least one digit."
            return render(request, 'signup.html', {"message": message})
        elif not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~]', adminpwd):
            message = "Password must contain at least one special character."
            return render(request, 'signup.html', {"message": message})
        check = User.objects.create_user(adminuname, adminemail, adminpwd)
        check.save()
        msg = "Account successfully created!!"
        return render(request, 'signup.html', {"message": msg})
    return render(request, 'signup.html')

def checkuserlogin(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        user1=(username,password)
        print(user1)
        n=username
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'customerapp/greeting.html',{"name":n})
        artist = Artist.objects.filter(Q(username=username) & Q(password=password)).first()
        if artist is not None:
            return render(request, 'artistapp/artisthome.html', {"name": n})
        else:
            adminuname=request.POST["uname"]
            adminpwd=request.POST["pwd"]
            flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
            print(flag)
            if flag:
                name=adminuname
                return render(request,'adminapp/adminhome.html',{"n":name})
            else:
                message="Invalid Credentials!!"
                return render(request,"login.html",{"msg":message})
    return render(request,"login.html")

def userlogout(request):
    return render(request,"login.html")

def userabout(request):
    return render(request, "customerapp/userabout.html")

def home1(request):
    products=Product.objects.all()
    return render(request, "customerapp/home1.html",{'products': products})

def pd1(request):
    return render(request, "customerapp/pd1.html")

def decontact(request):
    return render(request,"customerapp/decontact.html")

def adminlogout(request):
    return render(request,"login.html")

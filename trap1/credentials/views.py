from django.contrib import messages ,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info("invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Email= request.POST['Email']
        Password= request.POST['Password']
        Password1 = request.POST['Password1']
        if Password==Password1:
            if User.objects.filter(username=username).exists():
               messages.info(request,"Username taken")
               return redirect("register")
            elif User.objects.filter(email=Email).exists():
               messages.info(request,"email taken")
               return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=Password,first_name=Firstname,last_name=Lastname,email=Email)
                user.save();
                return redirect('login')
            print("user created")
        else:
              messages.info(request,"password not matching")
              return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
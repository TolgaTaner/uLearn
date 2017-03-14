from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import models

def register(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    password = request.POST.get('password')
    bdate = request.POST.get('bdate')
    user = User(username = email,email = email,first_name = name, last_name = surname, password = password)
    myuser = MyUser(user = user, birth_date = bdate)
    user.save()
    myuser.save()
    return render(request,'register.html')
    

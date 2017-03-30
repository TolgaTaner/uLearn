from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import models
from uLearnApp.forms import loginForm
from uLearnApp.models import MyUser
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login


def auth_login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')

            else:
                form = loginForm()
                return render(request, 'login.html', {'form': form})


    else:
        form = loginForm()
        return render(request, 'login.html', {'form': form})

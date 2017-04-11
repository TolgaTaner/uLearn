from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import models
from uLearnApp.forms import RegisterForm
from uLearnApp.models import MyUser
from django.forms import inlineformset_factory

def TeacherR(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            birth_date = form.cleaned_data['birth_date']
            user = User.objects.create_user(email, email = email, password = password, first_name = name, last_name = surname)
            form_user = form.save(commit = False)
            form_user.user = user
            form_user.birth_date = birth_date
            form_user.save()
            return HttpResponseRedirect('/')

        else:
            form = RegisterForm()
            return render(request, 'TeacherR.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'TeacherR.html', {'form': form})

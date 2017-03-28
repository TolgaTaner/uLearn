from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import models
from uLearnApp.forms import RegisterForm
from uLearnApp.models import MyUser
from django.forms import inlineformset_factory

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        user_formset = inlineformset_factory(User, MyUser , fields=('birth_date',))
        email = form.cleaned_data('email')
        password = form.cleaned_data('password')
        name = form.cleaned_data('name')
        surname = form.cleaned_data('surname')
        user = User.objects.create_user(email, email = email, password = password, first_name = name, last_name = surname)
        formset = user_formset(user = user)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/')


    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

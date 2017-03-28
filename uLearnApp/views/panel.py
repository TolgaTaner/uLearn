from django.shortcuts import render
from django.http import HttpResponse

def panel(request):
    return render(request,'panel.html')

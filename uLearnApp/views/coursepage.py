from django.shortcuts import render
from django.http import HttpResponse

def coursepage(request):
    return render(request,'coursepage.html')

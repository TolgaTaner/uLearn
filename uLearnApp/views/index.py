from django.shortcuts import render
from django.http import HttpResponse

def anaSayfa(request):
    return render(request,'index.html')

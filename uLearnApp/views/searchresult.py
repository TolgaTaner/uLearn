from django.shortcuts import render
from django.http import HttpResponse

def searchresult(request):
    return render(request,'searchresult.html')

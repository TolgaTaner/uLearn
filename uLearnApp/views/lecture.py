
from django.shortcuts import render
from django.http import HttpResponse

def lecture(request):
    return HttpResponse("Hello, world. You're at the polls index.")

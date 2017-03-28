from django.shortcuts import render
from django.http import HttpResponse

def courseInstructor(request):
    return render(request,'courseInstructor.html')

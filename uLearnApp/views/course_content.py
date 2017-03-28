from django.shortcuts import render
from django.http import HttpResponse

def course_content(request):
    return render(request,'course_content.html')

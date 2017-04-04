from django.shortcuts import render
from django.http import HttpResponse

def TeacherR(request):
    return render(request,'TeacherR.html')

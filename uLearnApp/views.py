from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    alican = 5
    return render(request,'index.html', {'ertan':alican})
def lecture(request):
    return HttpResponse("Hello, world. You're at the polls index.")

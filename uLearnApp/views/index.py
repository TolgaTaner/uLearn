from django.shortcuts import render
from django.http import HttpResponse

def anaSayfa(request):
    alican = 5
    return render(request,'index.html', {'ertan':alican})

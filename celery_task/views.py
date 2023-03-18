from django.shortcuts import render
from django.http import HttpResponse
from .task import *

# Create your views here.


def index(request):
    status = sleepy.delay(10)
    print("status", status)
    return HttpResponse("done")

from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse('Hello world')

from django.shortcuts import render

# Create your views here.

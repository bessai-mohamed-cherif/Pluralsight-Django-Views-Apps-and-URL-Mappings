from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello there, e-commerce store front coing through...")

def detail(request):
    return HttpResponse("detail")
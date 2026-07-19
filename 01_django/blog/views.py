from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("blog homepage !")

def about(request):
    a = 44
    return HttpResponse(f"Value of a is {a}\n blog about homepage")
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("shop homepage !")

def about(request):
    a = 44
    return HttpResponse(f"shop about homepage")

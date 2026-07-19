from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_details(request,pid):
    return HttpResponse(f"<h1>post id is {pid}<h1>")

def user_profile(request,username):
    return HttpResponse(f"<h1> USERNAME IS {username}.</h1>")

def date(request,year):
    return HttpResponse(f"<h1>Year is {year} </h1>")

def detail(request,**kwargs):
    return HttpResponse(f"<h1>Details : {kwargs}</h1>")
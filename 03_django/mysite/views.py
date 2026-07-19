from django.shortcuts import render   #render means run command

def home(request):
    return render(request,'home.html')
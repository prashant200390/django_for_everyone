from django.shortcuts import render
from datetime import datetime
# Create your views here.

class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def home(request):
    context = {
        'name' : "Prashant Kharel",
        'age' : 25 ,
        'skills' : ["python", "django", "react"],
        'user' : user('Kharel',23),
        'blog' : {
            'title' : "django templates intro",
            'content' : "<b> This is in Bold </b>",
            'created_at' : datetime(2026,7,16,9,30),
        },
        "empty_value" : None,
    }
    return render(request, 'home.html', context)
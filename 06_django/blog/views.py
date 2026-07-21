from django.shortcuts import render
from datetime import datetime
def blog_details(request):
    post = {
        "title" : "my second title post.",
        "description" : "django is a high level backend language .",
        "author" : None,
        "created_at" : datetime(2026,9,3,7,30),
        "comment_count" : 5,
        "tags" : ["python", "django" , "react.js"],
        "price" : 2500,
        "number" : 7 ,
        
    }
    return render(request,'blog_details.html',{"post": post})
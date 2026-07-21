from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    blog = [
        {'title': 'django basics', "is_featured": True , "author": "prashant kharel" },
        {'title': 'django advanced', "is_featured": False , "author": "" },
        {'title': 'django REST framework', "is_featured": False , "author": "ramu subedi" },
    ]
    context = {
        "blog" : blog,
        "today": datetime.now(),
        "html_code": "<h1>Welcome to my blog</h1>",
    }
    return render(request, 'blog_list.html', context)
from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html')

def blog(request):
    student_list = [
        {"name":"mohit","class":"10th"},
        {"name":"ramu","class":"10th"},
        {"name":"kaku","class":"10th"},
    ]
    return render(request,'blog.html',{"students":student_list})
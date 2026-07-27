from django.shortcuts import render
from .models import student
# Create your views here.
def home(request):
    students = student.objects.all()
    return render(request,'home.html',{"students":students})
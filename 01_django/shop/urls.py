from . import views
from django.urls import path

urlpatterns =[
    path('home2/',views.home,name='home'),
    path('about2/',views.about,name="about")
]
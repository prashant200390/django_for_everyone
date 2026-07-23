from django.urls import path
from . import views

urlpatterns = [
    path("blog/",views.home,name="home"),
    path('',views.base,name="base"),
]
from . import views
from django.urls import re_path , path 

urlpatterns = [
    path('post/<int:pid>', views.post_details, name="postdetails"),
    path('user/<str:username>', views.user_profile, name="userdetails"),
    re_path(r'^year/(?P<year>[0-9]{4})/$',views.date,name="date"),
    #for multiple arguments using path and kwargs
    path('detail/<int:year>/<str:month>/<str:founder>/',views.detail,name="detail"),
    
]
from django.urls import path 
from myapp.views import * 

urlpatterns =[
    path('',index,name="index"),
    path('log',log,name="log"),
    path('home',home,name="home"),
]
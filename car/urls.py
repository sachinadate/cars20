from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('carsell',views.carsell,name='carsell'),
    path('index',views.index,name='index'),
    path('getprice',views.getprice,name='getprice')
]
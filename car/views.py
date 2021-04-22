from django.shortcuts import render
from django.http import HttpResponse
from . import ML
import pandas as pd

# Create your views here.


def index(request):
    return render(request,'index.html')


def carsell(request):
    return render(request,'carsell.html',{'valid':False})

def getprice(request):
    cbrand=request.POST['cbrand']
    cyear=request.POST['cyear']
    clocation=request.POST['clocation']
    cfule=request.POST['inlineRadioOptions']
    ckm=request.POST['ckm']
    cmodel=request.POST['cmodel']

    xin=[cbrand,cfule,ckm,cmodel,clocation,cyear]


    
    #'Toyota','Diesel',1.0,'Prado','Karachi',1997.0    cbrand,cyear,clocation,cfule,ckm
    #ML(cbrand,cyear,clocation,cfule,ckm)
    #model

    return render(request,'carsell.html',{'price':(ML.fun(xin)/6).round(),'valid':True})





 #   return render(request,'carsell.html',{'price':ML.fun()})
    #return render(request,'carsell.html',{'price':ML(cbrand,cyear,clocation,cfule,ckm)})
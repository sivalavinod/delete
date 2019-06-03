import random

from django.contrib import messages
from django.shortcuts import render,redirect
from online import sendmessage
from .models import Client
from .forms import ClientForm


def clientReg(request):
    if request.method=="POST":
        name=request.POST.get("name")
        address=request.POST.get("address")
        username=request.POST.get("username")
        password=request.POST.get("password")
        photo=request.FILES["photo"]
        contact=request.POST.get("contact")
        otp="123456"
        Client(name=name,address=address,username=username,password=password,photo=photo,contact=contact,otp=otp).save()
        qs=Client.objects.all()
        res=ClientForm
        return render(request,"client/clientregi.html",{"data":qs,"form":res})
    else:
        return render(request,"")


def clientregi(request):
    res=ClientForm()
    qs = Client.objects.all()
    return render(request,"client/clientregi.html",{"form":res,"data":qs})


def clienthi(request):

    return render(request,"client/clienthi.html")


def logout(request):
    return render (request,"client/client_login.html")


def sendotp(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pswd=request.POST.get("password")
        cno=request.POST.get("contact")
        try:
            res=Client.objects.get(username=uname,password=pswd)
            if res:
                otp=random.randint(100000,999999)
                res.otp=otp
                res.save()
                message="hello cliet this is your otp:" +str(otp)
                d1=sendmessage.sendACAMS(cno,message)
                import json
                dd=json.load(d1)
                if dd["return"]:
                    return render(request,"client/otpvalidation.html")
                else:
                    messages.error(request,"sorry unable to send otp")
                    return render(request,"client/client_login.html")
        except:
            messages.error(request,"invalid user")
            return render(request, "client/client_login.html")
    else:
        return render(request, "client/client_login.html")


def otpvalidation(request):
    if request.POST:
        otp=request.POST.get("otp")
        try:
            Client.objects.get(otp=otp)
            request.session['sta']=True
            return render(request,"client/clienthi.html")
        except:
            messages.error(request,"please enter valid otp")
            return render(request,"otpvalidation.html")
    else:
        messages.error(request,"please enter valid username and password")
        return render(request,"client/client_login.html")

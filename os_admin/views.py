import random
from django.shortcuts import render,redirect
from .models import Admin,AgentRegister
from online import sendmessage
from django.contrib import messages


def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get("cno")
        upswd=request.POST.get("cpswd")
        try:
            res=Admin.objects.get(contact_no=uname,password=upswd)
            if res:
                print(res)
                otp=random.randint(100000,999999)
                res.otp=otp
                print(res.otp)
                res.save()
                message="hello admin this is your otp:" +str(otp)
                print(message)
                d1=sendmessage.sendACASMS(uname,message)
                import json
                dd=json.loads(d1)
                print(dd)
                if dd["return"]:
                    return render(request,"admin/otpvalidate.html")
                else:
                    messages.error(request,"sorry unable to send otp")
                    return render(request,"admin/admin_login.html")

        except:
            messages.error(request,"invalid user")
            return render(request, "admin/admin_login.html")
    else:
        return render(request, "admin/admin_login.html")


def otpvalidation(request):
    if request.POST:
        otp=request.POST.get("otp")
        try:
            Admin.objects.get(otp=otp)
            request.session['sta']=True
            #request.session.set_expiry(60)
            return render(request,"admin/admin_welcome.html")
        except:
            messages.error(request,"please enter valid otp")
            return render(request,"admin/admin_login.html")
    else:
        return render(request,"admin/admin_login.html")


def agentdatasave(request):
    if request.method == "POST":
        ano=request.POST.get("agno")
        aname=request.POST.get("name")
        acno=request.POST.get("cno")
        add=request.POST.get("add")
        image=request.FILES["image"]
        uname=request.POST.get("uname")
        pword=request.POST.get("pword")
        otp=12335
        AgentRegister(agent_no=ano,name=aname,contact_no=acno,address=add,photo=image,username=uname,password=pword,otp=otp).save()
        qs=AgentRegister.objects.all()
        return render(request,"admin/welcome_admin.html",{"data":qs})
    else:
        return redirect('/admin_admin/agentdatasave/')



def agent_delete(request):
    name = request.GET.get("username")
    AgentRegister.objects.get(username=name).delete()
    qs = AgentRegister.objects.all()
    return render(request, "admin/welcome_admin.html", {"data": qs})



def agentelcome(request):
    qs = AgentRegister.objects.all()
    return render(request, "admin/welcome_admin.html", {"data": qs})


def logoutadmin(request):
    request.session['sta']=False
    return render(request,"admin/welcome_admin.html")
from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
from cheif.models import Cheif
from additionals.models import Additionals

# Create your views here.

def login(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        obj=Login.objects.filter(username=uname,password=pwd)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.uid
            if tp=="admin":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp=="cheif":
                ob=Cheif.objects.get(cheif_id=uid)
                if ob.status=="Approved":
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/chief/')
                else:
                    message="Your Registration is pending"
                    context={
                        'msg':message
                    }
                    return render(request,'login/login.html',context)
            elif tp=="additional":
                ob=Additionals.objects.get(additional_id=uid)
                if ob.status=="accepted":
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/additional/')
                else:
                    message="Your Registration is pending"
                    context={
                        'msg':message
                    }
                    return render(request,'login/login.html',context)
            else:
                message = "Incorrect username and password"
                context = {
                    'msg': message
                }
            return render(request, 'login/login.html', context)
    return render(request, 'login/login.html')


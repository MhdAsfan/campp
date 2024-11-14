from django.shortcuts import render
from cheif.models import Cheif
from login.models import Login
from django.http import  HttpResponseRedirect
# Create your views here.
def cheifreg(request):
    if request.method =='POST':
        uname = request.POST.get('uname')
        password = request.POST.get('ps')
        cpassword = request.POST.get('cpwd')
        if Login.objects.filter(username=uname).exists():
            message = "Username already exists"
            context = {
                'msg': message
            }
            return render(request, 'cheif/cheifreg.html', context)
        elif password == cpassword:
            obj = Cheif()
            obj.name = request.POST.get('un')
            obj.username = request.POST.get('uname')
            obj.password = request.POST.get('ps')
            obj.email_id = request.POST.get('email')
            obj.phone_no = request.POST.get('ph')
            obj.collegename = request.POST.get('cn')
            obj.totelpapers=1
            obj.status = 'pending'
            obj.save()
            obj1 = Login()
            obj1.username = obj.username
            obj1.password = obj.password
            obj1.type = 'cheif'
            obj1.uid = obj.cheif_id
            obj1.save()
            return HttpResponseRedirect('/temp/home/')
        else:
            message = 'Password and confirm password is missmatch....'
            context = {
                'msg': message
            }
            return render(request, 'cheif/cheifreg.html', context)
    return render(request, 'cheif/cheifreg.html')

def view_admin_manage_cheif(request):
    obj = Cheif.objects.all()
    context = {
        'a': obj,
    }
    return render(request,'cheif/view_admin_manage_cheif.html',context)

def accept(request,idd):
    obj=Cheif.objects.get(cheif_id=idd)
    obj.status="Approved"
    obj.save()
    return view_admin_manage_cheif(request)

def reject(request,idd):
    obj=Cheif.objects.get(cheif_id=idd)
    obj.status="Denied"
    obj.save()
    return view_admin_manage_cheif(request)
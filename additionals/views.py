from django.shortcuts import render
from additionals.models import Additionals
from course.models import Course
from login.models import Login
from django.http import  HttpResponseRedirect
from paper.models import Paper
# Create your views here.
def additionalreg(request):
    obb=Course.objects.all()
    obj=Paper.objects.all()
    context={
        'a':obb,
        'p':obj
    }
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('ps')
        cpassword = request.POST.get('cpwd')
        if Login.objects.filter(username=uname).exists():
            message = "Username already exists"
            context = {
                'msg': message
            }
            return render(request, 'additionals/additionalreg.html', context)
        elif password == cpassword:
            obj = Additionals()
            obj.name = request.POST.get('un')
            obj.username = uname
            obj.password = password
            obj.email_id = request.POST.get('email')
            obj.phone_no = request.POST.get('ph')
            obj.uid = 1
            obj.course_id = request.POST.get('course')
            obj.sem = request.POST.get('sem')
            obj.priority_1 = request.POST.get('priority1')
            obj.priority_2 = request.POST.get('priority2')
            obj.priority_3 = request.POST.get('priority3')
            obj.collegename=request.POST.get('cn')
            obj.totelpapers =1
            obj.status = "pending"
            obj.save()
            obj1 = Login()
            obj1.username = obj.username
            obj1.password = obj.password
            obj1.type = 'additional'
            obj1.uid = obj.additional_id
            obj1.save()
            return HttpResponseRedirect('/temp/home/')
        else:
            message = 'Password and confirm password is missmatch....'
            context = {
                'msg': message
            }
            return render(request, 'additionals/additionalreg.html', context)
    return render(request, 'additionals/additionalreg.html',context)



def view_admin_manage_additionl(request):
    obj = Additionals.objects.all()
    context = {
        'c': obj,
    }
    return render(request,'additionals/view_admin_manage_additionl.html', context)

def acceptadmin(request, idd):
    obj = Additionals.objects.get(additional_id=idd)
    obj.status = 'accepted'
    obj.save()
    return view_admin_manage_additionl(request)

def rejectadmin(request, idd):
    obj = Additionals.objects.get(additional_id=idd)
    obj.status = 'rejected'
    obj.save()
    return view_admin_manage_additionl(request)


def view_admin_view_additional_profile(request):
    obj = Additionals.objects.all()
    context ={
        'a': obj,
    }
    return render(request, 'additionals/view_admin_view_additional_profile.html',context)


def view_cheif_manage_additionals(request):
    obj = Additionals.objects.all()
    context = {
        'b': obj,
    }
    return render(request, 'additionals/view_cheif_manage_additionals.html',context)


def accept(request,idd):
    obj=Additionals.objects.get(additional_id=idd)
    obj.status="Approved"
    obj.save()
    return view_cheif_manage_additionals(request)



def reject(request,idd):
    obj=Additionals.objects.get(additional_id=idd)
    obj.status="Denied"
    obj.save()
    return view_cheif_manage_additionals(request)

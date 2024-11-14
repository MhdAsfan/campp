from django.shortcuts import render
from form.models import Form
# Create your views here.
def view_additional_view_form(request):
    obj = Form.objects.all()
    context = {
        'a': obj,
    }
    return render(request, 'form/view_additional_view_form.html',context)


def view_admin_manage_form(request):
    obj = Form.objects.all()
    context = {
        'b': obj,
    }
    return render(request, 'form/view_admin_manage_form.html',context)


def view_chief_manage_form(request):
    obj = Form.objects.all()
    context = {
        'c': obj,
    }
    return render(request, 'form/view_chief_manage_form.html',context)

def accept(request,idd):
    obj=Form.objects.get(form_id=idd)
    obj.status="Approved"
    obj.save()
    return view_admin_manage_form(request)

def reject(request,idd):
    obj=Form.objects.get(form_id=idd)
    obj.status="Denied"
    obj.save()
    return view_admin_manage_form(request)




def accept1(request,idd):
    obj=Form.objects.get(form_id=idd)
    obj.status="Approved"
    obj.save()
    return view_chief_manage_form(request)

def reject1(request,idd):
    obj=Form.objects.get(form_id=idd)
    obj.status="Denied"
    obj.save()
    return view_chief_manage_form(request)
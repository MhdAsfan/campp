from django.shortcuts import render
from paper.models import Paper
from course.models import Course
from cheif.models import  Cheif

# Create your views here.
def postpaper(request):
    obb=Course.objects.all()
    context={
        "qw":obb
    }

    if request.method == "POST" :
        obb = Paper()
        obb.sem = request.POST.get ("sem")
        obb.paper = request.POST.get("paper")
        obb.course_id = request.POST.get("crs")
        obb.status = 'pending'
        obb.save()
    return render(request,'paper/postpaper.html',context)

def view_additional_view_paper_details(request):
    obj = Paper.objects.all()
    context = {
        'a': obj,
    }
    return render(request, 'paper/view_additional_view_paper_details.html',context)

def view_admin_manage_paper(request):
    obj = Paper.objects.all()
    context = {
        'b': obj,
    }
    return render(request, 'paper/view_admin_manage_paper.html',context)

def view_admin_view_paper_details(request):
    obj = Paper.objects.all()
    context = {
        'c': obj,
    }
    return render(request, 'paper/view_admin_view_paper_details.html',context)

def view_chief_completed_status(request):
    obj = Paper.objects.all()
    context = {
        'd': obj,
    }
    return render(request, 'paper/view_chief_completed_status.html',context)

def view_chief_view_paper(request):
    obj = Paper.objects.all()
    context = {
        'e': obj,
    }
    return render(request, 'paper/view_chief_view_paper.html',context)



def accept(request,idd):
    obj=Paper.objects.get(paper_id=idd)
    obj.status="Approved"
    obj.save()
    return view_admin_manage_paper(request)

def reject(request,idd):
    obj=Paper.objects.get(paper_id=idd)
    obj.status="Denied"
    obj.save()
    return view_admin_manage_paper(request)

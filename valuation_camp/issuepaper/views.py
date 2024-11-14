from django.shortcuts import render
from cheif.models import Cheif
from paper.models import Paper
from issuepaper.models import IssuePaper,AssignPaper,ChiefIssuepaperAdditional
from additionals.models import Additionals
from django.db.models import Q
# Create your views here.



def add_issuepaper(request):
    obj = Paper.objects.all()
    ob=Cheif.objects.filter(status="Approved")
    context = {

        'p': obj,
        "c":ob
    }
    if request.method == "POST":
        obb = IssuePaper()
        obb.paper_id = request.POST.get("paper")
        obb.cheif_id = request.POST.get("chief")
        obb.start = request.POST.get("Start")
        obb.end = request.POST.get("End")
        obb.status = 'pending'
        obb.save()

    return render(request, 'issuepaper/issuepaper.html', context)

def view_chief_issue_paper(request):
    uid=request.session["u_id"]
    ob = Paper.objects.all()
    on=Additionals.objects.all()
    obj = IssuePaper.objects.filter(cheif_id=uid)
    context = {
        'p': obj,
        'y':ob,
        'z':on
    }
    if request.method=='POST':
        om=ChiefIssuepaperAdditional()
        om.start=request.POST.get('Start')
        om.end = request.POST.get('End')
        om.paper_id=request.POST.get('paper')
        om.additional_id = request.POST.get('Additionals')
        om.cheif_id=uid
        om.status='pending'
        om.save()
    return render(request, 'issuepaper/chief_view_issued_paper.html', context)


def view_addiional_list(request,idd):
    ob=IssuePaper.objects.get(work_id=idd)
    obj = Additionals.objects.filter(Q (priority_1=ob.paper.paper) | Q (priority_2=ob.paper.paper) | Q (priority_3=ob.paper.paper) )
    context = {
        'a': obj,
    }
    return render(request, 'issuepaper/viiew_additional_list.html', context)



def post_assign(request,idd):
    if request.method=="POST":
        obj = Additionals.objects.get(additional_id=idd)
        ob=AssignPaper()
        ob.additional_id=idd
        ob.issuepaper_id=request.session["issue_id"]
        ob.start = request.POST.get("Start")
        ob.end = request.POST.get("End")
        ob.status="pending"
        ob.save()
        return view_chief_issue_paper(request)

    return render(request, 'issuepaper/post_additional_assign.html')



def additional_view_assign_paper(request):
    uid=request.session["u_id"]
    ob=ChiefIssuepaperAdditional.objects.filter(additional_id=uid)
    context={
        'x':ob
    }
    return render(request,'issuepaper/Additional_view_assign_paper.html',context)

def assigncompleted(request,idd):

    if request.method=="POST":
        obj = ChiefIssuepaperAdditional.objects.get(work_id=idd)
        stno=obj.start
        endno=obj.end
        tot=endno-stno
        adobj=Additionals.objects.get(additional_id=obj.additional_id)
        adobj.totelpapers=adobj.totelpapers+tot
        adobj.save()
        chobj=Cheif.objects.get(cheif_id=obj.cheif_id)
        chobj.totelpapers=chobj.totelpapers+tot
        chobj.save()
        obj.status = "Approved"
        obj.save()

        return additional_view_assign_paper(request)



    return render(request,'issuepaper/assigncompleted.html')

def Adminview_assignpaper(request):
    ob = AssignPaper.objects.all()
    context = {
        'x': ob
    }
    return render(request,'issuepaper/Adminview_assignpaper.html',context)


def Chiefview_assignpaper(request):
    # uid=request.session["u_id"]
    ob = IssuePaper.objects.all()
    context = {
        'x': ob
    }
    return render(request,'issuepaper/Chiefview_assignpaper.html',context)


def chief_aditional_status(request):
    # uid=request.session["u_id"]
    ob = ChiefIssuepaperAdditional.objects.all()
    context = {
        'x': ob
    }
    return render(request,'issuepaper/chief_view_additional_paper_status.html',context)
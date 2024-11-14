from django.shortcuts import render
from work.models import Work
from assign.models import Assign
import datetime
# Create your views here.
def workdistributionbychef(request,idd):
    obb=Assign.objects.get(assign_id=idd)
    context = {
        'a':obb
    }
    if request.method == 'POST':
        obj = Work()
        obj.count = request.POST.get('count')
        obj.date = datetime.datetime.today()
        obj.assign_id=idd
        obj.from_field = request.POST.get('from')
        obj.to = request.POST.get('to')
        obj.status="Pending"
        obj.save()
    return render(request, 'work/workdistributionbycheif.html',context)


def vw_work(request):
    obj=Work.objects.all()
    context={
        'a':obj
    }
    return render(request,'work/work view.html',context)
def vw_com(request):
    obj=Work.objects.filter(status="completed")
    context={
        'a':obj
    }
    return render(request,'work/completed.html',context)
def status(request,idd):
    if request.method=="POST":
        obj=Work.objects.get(work_id=idd)
        obj.status=request.POST.get('status')
        obj.save()
    return render(request,'work/status.html')
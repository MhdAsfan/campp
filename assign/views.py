from django.shortcuts import render
from assign.models import Assign
from additionals.models import Additionals
from paper.models import Paper

# Create your views here.
def assign(request,idd):
    ob=Paper.objects.all()
    obv=Additionals.objects.get(additional_id=idd)
    context={
        'a':ob,
        'v':obv
    }
    if request.method=='POST':
        obj=Assign()
        obj.additional_id= idd
        obj.paper_id=request.POST.get('priority1')
        obj.status='pending'
        obj.save()
    # ob = Additionals.objects.all()
    # ob2 = Paper.objects.all()

    return render(request, 'assign/assign.html',context)


def view_additional_view_assign(request):
    obj = Assign.objects.all()
    context = {
        'a': obj,
    }
    return render(request, 'assign/view_additional_view_assign.html',context)
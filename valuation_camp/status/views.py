from django.shortcuts import render
from status.models import Status

# Create your views here.
def additonalstatus(request):
    if request.method == 'POST':
        obj = Status()
        obj.count_id = request.POST.get('count')
        obj.check_id = request.POST.get('check')
        obj.date_time_id = request.POST.get('date')
        obj.save()
    return render(request, 'status/additionalstatus.html')
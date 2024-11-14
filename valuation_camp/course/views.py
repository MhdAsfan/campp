from django.shortcuts import render
from course.models import Course

# Create your views here.
def course(request):
    if request.method == 'POST':
        obj = Course()
        obj.course = request.POST.get('ca')
        obj.save()
    return render(request,'course/course.html')

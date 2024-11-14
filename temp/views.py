from django.shortcuts import render

# Create your views here.
def admin_home(request):
    return render(request,'temp/admin.html')

def additional_home(request):
    return render(request,'temp/Additional.html')

def chief_home(request):
    return render(request,'temp/cheif.html')

def home(request):
    return render(request,'temp/home.html')
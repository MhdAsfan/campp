from django.conf.urls import url
from temp import views

urlpatterns = [
    url('admin/', views.admin_home),
    url('additional/', views.additional_home),
    url('chief/', views.chief_home),
    url('home/', views.home),



]
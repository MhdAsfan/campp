from django.conf.urls import url
from . import views

urlpatterns = [
    url('bill/',views.bill),
    url('aaaa/',views.chief_view)

]
from django.conf.urls import url
from . import views

urlpatterns = [
    url('work/(?P<idd>\w+)',views.workdistributionbychef),
    url('vw/',views.vw_work),
    url('sts/(?P<idd>\w+)',views.status),
    url('cmp/',views.vw_com)

]
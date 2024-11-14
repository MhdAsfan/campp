from django.conf.urls import url
from . import views

urlpatterns = [

    url('cheifreg/',views.cheifreg),
    url('view_admin_manage_cheif/',views.view_admin_manage_cheif),

    url('accept/(?P<idd>\w+)', views.accept),
    url('reject/(?P<idd>\w+)', views.reject),

]
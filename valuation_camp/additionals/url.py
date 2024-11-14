from django.conf.urls import url
from . import views

urlpatterns = [
    url('additionalreg/', views.additionalreg),
    url('view_admin_manage_additionl/',views.view_admin_manage_additionl),
    url('view_admin_view_additional_profile/',views.view_admin_view_additional_profile),
    url('view_cheif_manage_additionals/',views.view_cheif_manage_additionals),

    url('acceptadmin/(?P<idd>\w+)', views.acceptadmin),
    url('rejectadmin/(?P<idd>\w+)', views.rejectadmin),

    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),


]



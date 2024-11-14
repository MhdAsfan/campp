from django.conf.urls import url
from . import views

urlpatterns = [
    url('view_additional_view_form/',views.view_additional_view_form),
    url('view_admin_manage_form',views.view_admin_manage_form),
    url('v_c_mf',views.view_chief_manage_form),

    url('accept/(?P<idd>\w+)', views.accept),
    url('reject/(?P<idd>\w+)', views.reject),

    url('accept1/(?P<idd>\w+)',views.accept1),
    url('reject1/(?P<idd>\w+)',views.reject1),

]
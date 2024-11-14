from django.conf.urls import url
from . import views

urlpatterns = [

    url('postpaper',views.postpaper),
    url('view_additional_view_paper_details',views.view_additional_view_paper_details),
    url('view_admin_manage_paper',views.view_admin_manage_paper),
    url('view_admin_view_paper_details',views.view_admin_view_paper_details),
    url('view_chief_completed_status',views.view_chief_completed_status),
    url('view_chief_view_paper',views.view_chief_view_paper),

    url('accept/(?P<idd>\w+)', views.accept),
    url('reject/(?P<idd>\w+)', views.reject),
]
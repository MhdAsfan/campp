from django.conf.urls import url
from . import views

urlpatterns = [
    url('issuepaper',views.add_issuepaper),
    url('cv_ip',views.view_chief_issue_paper),

    url('view_additional/(?P<idd>\w+)', views.view_addiional_list),
    url('post/(?P<idd>\w+)', views.post_assign),

    url('additional_view_assign_paper',views.additional_view_assign_paper),
    url('assigncompleted/(?P<idd>\w+)',views.assigncompleted),
    url('Adminview_assignpaper',views.Adminview_assignpaper),
    url('Chiefview_assignpaper',views.Chiefview_assignpaper),
    url('chief_aditional_status/',views.chief_aditional_status),

]

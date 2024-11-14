from django.conf.urls import url
from . import views

urlpatterns = [
    url('assign/(?P<idd>\w+)',views.assign),
    url('view_additional_view_assign/',views.view_additional_view_assign),

]
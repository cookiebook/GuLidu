from django.urls import path, include
from orgs.views import *

app_name = 'orgs'
urlpatterns = [
    path('org_list/$', org_list, name='org_list'),
    path('org_detail/<int:org_id>/$', org_detail, name='org_detail'),
    path('org_detail_course/<int:org_id>/$', org_detail_course, name='org_detail_course'),
    path('org_detail_desc/<int:org_id>/$', org_detail_desc, name='org_detail_desc'),
    path('org_detail_teacher/<int:org_id>/$', org_detail_teacher, name='org_detail_teacher'),

    path('teachers_list/$', teachers_list, name='teachers_list'),
    path('teacher_detail/<int:teacher_id>/$', teacher_detail, name='teacher_detail'),
    # path('org_detail_teacher/<int:org_id>/$', org_detail_teacher, name='org_detail_teacher'),
    # path('user_login/$', user_login, name='user_login'),
    # path('user_forget/$', user_forget, name='user_forget'),
    # path('user_reset/<str:code>', user_reset, name='user_reset'),
    # path('user_logout/$', user_logout, name='user_logout'),
    # path('user_active/<str:code>', user_active, name='user_active'),
]
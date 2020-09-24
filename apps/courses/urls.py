from django.urls import path, include
from courses.views import *

app_name = 'courses'
urlpatterns = [
    path('courses_list/$', courses_list, name='courses_list'),
    path('courses_detail/<int:course_id>/$', courses_detail, name='courses_detail'),
    path('courses_video/<int:course_id>/$', courses_video, name='courses_video'),
    path('courses_comment/<int:course_id>/$', courses_comment, name='courses_comment'),
    # path('user_login/$', user_login, name='user_login'),
    # path('user_forget/$', user_forget, name='user_forget'),
    # path('user_reset/<str:code>', user_reset, name='user_reset'),
    # path('user_logout/$', user_logout, name='user_logout'),
    # path('user_active/<str:code>', user_active, name='user_active'),
]
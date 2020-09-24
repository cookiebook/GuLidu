from django.urls import path, include
from operations.views import *

app_name = 'operations'
urlpatterns = [
    path('user_ask/$', user_ask, name='user_ask'),
    path('user_love/$', user_love, name='user_love'),
    path('user_comment/<int:course_id>/$', user_comment, name='user_comment'),
]
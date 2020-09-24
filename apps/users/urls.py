from django.urls import path, include
from users.views import *

app_name = 'users'
urlpatterns = [
    path('user_register/$', user_register, name='user_register'),
    path('user_login/$', user_login, name='user_login'),
    path('user_forget/$', user_forget, name='user_forget'),
    path('user_reset/<str:code>', user_reset, name='user_reset'),
    path('user_logout/$', user_logout, name='user_logout'),
    path('user_active/<str:code>', user_active, name='user_active'),
]

# http://127.0.0.1:8000/users/user_reset/MARsUkGo  # 修改密码链接

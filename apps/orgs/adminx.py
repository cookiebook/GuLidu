import xadmin
from django.db import models
from orgs.models import CityInfo, OrgInfo, TeacherInfo


class CityInfoAdminx(object):
    list_display = ['name', 'add_time']
    model_icon = 'fa fa-gift'


class OrgInfoAdminx(object):
    list_display = ['image', 'name', 'course_num', 'study_num', 'address',
                    'desc', 'detail', 'love_num', 'click_num', 'category',
                    'cityinfo', 'add_time']


class TeacherInfoAdminx(object):
    list_display = ['image', 'name', 'work_year', 'work_psoition', 'work_style',
                    'work_company', 'age', 'gender', 'love_num', 'click_num',
                    'add_time']


xadmin.site.register(CityInfo, CityInfoAdminx)
xadmin.site.register(OrgInfo, OrgInfoAdminx)
xadmin.site.register(TeacherInfo, TeacherInfoAdminx)

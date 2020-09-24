from django.shortcuts import render

from operations.models import UserLove
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

PAGESIZE = 2


def org_list(request):
    all_orgs = OrgInfo.objects.all().order_by('-love_num')
    all_citys = CityInfo.objects.all()
    sort_orgs = all_orgs.order_by('-love_num')[:3]

    pagenum = request.GET.get('page', '')
    cate = request.GET.get('cate', '')
    cityid = request.GET.get('cityid', '')
    sort = request.GET.get('sort', '')
    if cate:
        all_orgs = all_orgs.filter(category=cate)
    if cityid:
        all_orgs = all_orgs.filter(cityinfo_id=int(cityid))
    if sort:
        all_orgs = all_orgs.order_by("-" + sort)

    pa = Paginator(all_orgs, PAGESIZE)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request, 'orgs/org-list.html',
                  {'all_orgs': all_orgs,
                   'all_citys': all_citys,
                   'sort_orgs': sort_orgs,
                   'pages': pages,
                   'cate': cate,
                   'cityid': cityid,
                   'sort': sort})


def org_detail(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=org_id)[0]
        org.love_num += 1
        org.save()
        love_status = False
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=org_id, love_type='1', love_status=True)
            if love:
                love_status = True
        if org:
            return render(request, "orgs/org-detail-homepage.html",
                          {'org': org, 'detail_type': 'home', 'love_status': love_status})


def org_detail_course(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=org_id)[0]
        all_course = org.courseinfo_set.all()

        love_status = False
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=org_id, love_type='1', love_status=True)
            if love:
                love_status = True

        pagenum = request.GET.get('page', '')
        pa = Paginator(all_course, 1)
        try:
            pages = pa.page(pagenum)
        except PageNotAnInteger:
            pages = pa.page(1)
        except EmptyPage:
            pages = pa.page(pa.num_pages)
        if org:
            return render(request, "orgs/org-detail-course.html",
                          {'org': org, 'pages': pages, 'detail_type': 'course', 'love_status': love_status})


def org_detail_desc(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=org_id)[0]

        love_status = False
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=org_id, love_type='1', love_status=True)
            if love:
                love_status = True
        if org:
            return render(request, "orgs/org-detail-desc.html",
                          {'org': org, 'detail_type': 'desc', 'love_status': love_status})


def org_detail_teacher(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=org_id)[0]

        love_status = False
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=org_id, love_type='1', love_status=True)
            if love:
                love_status = True
        if org:
            return render(request, "orgs/org-detail-teachers.html",
                          {'org': org, 'detail_type': 'teachers', 'love_status': love_status})


def teachers_list(request):
    all_teacher = TeacherInfo.objects.all().order_by('-click_num')
    sort_teacher = all_teacher.order_by('-love_num')[:5]

    pagenum = request.GET.get('page', '')
    sort = request.GET.get('sort', '')
    if sort:
        all_teacher = all_teacher.order_by("-" + sort)

    pa = Paginator(all_teacher, 1)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request, 'orgs/teachers-list.html', {'all_teacher': all_teacher,
                                                       'sort_teacher': sort_teacher,
                                                       'sort': sort,
                                                       'pages': pages
                                                       })


def teacher_detail(request, teacher_id):
    if teacher_id:
        teacher = TeacherInfo.objects.filter(id=teacher_id)[0]
        teacher.click_num += 1
        teacher.save()
        sort_teacher = TeacherInfo.objects.all().order_by('-love_num')[:5]

        teacher_love_status = False
        org_love_status = False
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=teacher_id, love_type='3', love_status=True)
            if love:
                teacher_love_status = True
            love = UserLove.objects.filter(love_man=request.user, love_id=teacher.work_company.id, love_type='1',
                                           love_status=True)
            if love:
                org_love_status = True
        return render(request, 'orgs/teacher-detail.html', {'teacher': teacher,
                                                            'sort_teacher': sort_teacher,
                                                            'teacher_love_status': teacher_love_status,
                                                            'org_love_status': org_love_status})

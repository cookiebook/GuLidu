from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render

from operations.forms import UserCommentForm
from operations.models import UserLove, UserCourse, UserComment
from .models import *


def courses_list(request):
    all_course = CourseInfo.objects.all().order_by('-add_time')
    sort = request.GET.get('sort', '')
    if sort:
        all_course = all_course.order_by('-' + sort)
    remonment_course = all_course.order_by('-add_time')[:3]

    pagenum = request.GET.get('page', '')
    pa = Paginator(all_course, 1)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request, 'courses/course-list.html', {'all_course': all_course,
                                                        'remonment_course': remonment_course,
                                                        'pages': pages, 'sort': sort})


def courses_detail(request, course_id):
    if course_id:
        course = CourseInfo.objects.filter(id=course_id)[0]
        course.click_num += 1
        course.save()
        relate_course = CourseInfo.objects.filter(category=course.category).exclude(id=course_id)

        course_love_status = False
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=course_id, love_type='2', love_status=True)
            if love:
                course_love_status = True

        org_love_status = False
        if request.user.is_authenticated and course:
            love = UserLove.objects.filter(love_man=request.user, love_id=course.orginfo.id, love_type='1',
                                           love_status=True)
            if love:
                org_love_status = True

        return render(request, 'courses/course-detail.html',
                      {'course': course, 'relate_course': relate_course,
                       'course_love_status': course_love_status,
                       'org_love_status': org_love_status})


def courses_video(request, course_id):
    if course_id and request.user.is_authenticated:
        course = CourseInfo.objects.filter(id=course_id)[0]
        usercourse_list = UserCourse.objects.filter(study_man=request.user, study_course=course_id)
        if not usercourse_list:
            usercourse_list = UserCourse.objects.filter(study_man=request.user)
            courses_list = [user_course.study_course for user_course in usercourse_list]
            org_list = [course.orginfo for course in courses_list]
            if course.orginfo not in org_list:
                course.orginfo.study_num += 1
                course.orginfo.save()

            a = UserCourse()
            a.study_man = request.user
            a.study_course = course
            a.save()
            course.study_num += 1
            course.save()

        usercourse_list = UserCourse.objects.filter(study_course=course)
        user_list = [user_course.study_man for user_course in usercourse_list]
        usercourse_list = UserCourse.objects.filter(study_man__in=user_list).exclude(study_course=course)
        courses_list = list(set([user_course.study_course for user_course in usercourse_list]))

        return render(request, 'courses/course-video.html', {'course': course, 'courses_list': courses_list})
    else:
        return render(request, 'users/login.html')


def courses_comment(request, course_id):
    if course_id and request.user.is_authenticated:
        user_comment_form = UserCommentForm()
        course = CourseInfo.objects.filter(id=course_id)[0]

        usercourse_list = UserCourse.objects.filter(study_course=course)
        user_list = [user_course.study_man for user_course in usercourse_list]
        usercourse_list = UserCourse.objects.filter(study_man__in=user_list).exclude(study_course=course)
        courses_list = list(set([user_course.study_course for user_course in usercourse_list]))

        comment_list = course.usercomment_set.all()[:10]
        return render(request, 'courses/course-comment.html',
                      {'user_comment_form': user_comment_form, 'course': course, 'courses_list': courses_list,
                       'comment_list': comment_list})

from django.shortcuts import render

from orgs.models import OrgInfo, TeacherInfo
from .forms import UserAskForm, UserCommentForm
from .models import *
from django.http import JsonResponse


def user_ask(request):
    user_ask_form = UserAskForm(request.POST)
    if user_ask_form.is_valid():
        user_ask_form.save()
        return JsonResponse({'status': 'ok', 'msg': '咨询成功'})
    else:
        print(user_ask_form.errors)
        return JsonResponse({'status': 'fail', 'msg': '咨询失败'})


def user_love(request):
    love_id = request.GET.get('love_id', '')
    love_type = request.GET.get('love_type', '')
    obj = None
    if love_type == '1':
        obj = OrgInfo.objects.filter(id=int(love_id))[0]
    elif love_type == '2':
        obj = CourseInfo.objects.filter(id=int(love_id))[0]
    else:
        obj = TeacherInfo.objects.filter(id=int(love_id))[0]
    if love_id and love_type and obj:
        love = UserLove.objects.filter(love_id=int(love_id), love_type=love_type, love_man=request.user)
        if love:
            if love[0].love_status:
                love[0].love_status = False
                love[0].save()
                obj.love_num -= 1
                obj.save()
                return JsonResponse({'status': 'ok', 'msg': '收藏'})

            else:
                love[0].love_status = True
                love[0].save()
                obj.love_num += 1
                obj.save()
                return JsonResponse({'status': 'ok', 'msg': '取消收藏'})
        else:
            a = UserLove()
            a.love_status = True
            a.love_type = love_type
            a.love_id = love_id
            a.love_man = request.user
            a.save()
            obj.love_num += 1
            obj.save()
            return JsonResponse({'status': 'ok', 'msg': '取消收藏'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '失败'})


def user_comment(request, course_id):
    if course_id and request.user.is_authenticated:
        user_comment_form = UserCommentForm(request.POST)
        if user_comment_form.is_valid():
            a = UserComment()
            a.comment_man = request.user
            a.comment_content = user_comment_form.cleaned_data['comment_content']
            a.comment_course_id = user_comment_form.cleaned_data['comment_course']
            a.save()
            return JsonResponse({'status': 'ok', 'msg': '评论成功'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '评论失败'})

    else:
        return JsonResponse({'status': 'fail', 'msg': '用户未登录'})

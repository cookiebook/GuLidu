import xadmin
from datetime import datetime

from django.db import models

from operations.models import UserAsk, UserLove, UserCourse, UserComment, UserMessage
from users.models import UserProfile
from courses.models import CourseInfo


class UserAskAdminx(object):
    list_display = ['name', 'phone', 'course', 'add_time']


# 收藏表
class UserLoveAdminx(object):
    list_display = ['love_man', 'love_id', 'love_type', 'course', 'love_status', 'add_time']


# 学习课程
class UserCourseAdminx(object):
    list_display = ['study_man', 'study_course', 'add_time']


# 用户评论
class UserCommentAdminx(object):
    list_display = ['comment_man', 'comment_course', 'comment_content', 'add_time']
    comment_man = models.ForeignKey(UserProfile, verbose_name="评论用户", on_delete=models.DO_NOTHING)
    comment_course = models.ForeignKey(CourseInfo, verbose_name="评论课程", on_delete=models.DO_NOTHING)
    comment_content = models.CharField(max_length=300, verbose_name="评论内容")
    add_time = models.DateTimeField(verbose_name="评论时间", default=datetime.now)


# 用户消息
class UserMessageAdminx(object):
    list_display = ['message_man', 'message_content', 'message_status', 'add_time']
    message_man = models.IntegerField(default=0, verbose_name="消息用户")
    message_content = models.CharField(max_length=200, verbose_name="消息内容")
    message_status = models.BooleanField(default=False, verbose_name='消息状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")


xadmin.site.register(UserAsk, UserAskAdminx)
xadmin.site.register(UserLove, UserLoveAdminx)
xadmin.site.register(UserCourse, UserCourseAdminx)
xadmin.site.register(UserComment, UserCommentAdminx)
xadmin.site.register(UserMessage, UserMessageAdminx)

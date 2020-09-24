import xadmin
from courses.models import CourseInfo, LessonInfo, VideoInfo, SourceInfo


class CourseInfoAdminx(object):
    list_display = ['image', 'name', 'study_time', 'study_num', 'level', 'love_num', 'click_num',
                    'desc', 'detail', 'category', 'course_notice', 'course_need', 'teacher_tell',
                    'orginfo', 'teacherinfo', 'add_time']


class LessonInfoAdminx(object):
    list_display = ['name', 'course']


class VideoInfoAdminx(object):
    list_display = ['name', 'study_time', 'url', 'lessoninfo', 'add_time']


class SourceInfoAdminx(object):
    list_display = ['name', 'down_load', 'cource', 'add_time']


xadmin.site.register(CourseInfo, CourseInfoAdminx)
xadmin.site.register(LessonInfo, LessonInfoAdminx)
xadmin.site.register(VideoInfo, VideoInfoAdminx)
xadmin.site.register(SourceInfo, SourceInfoAdminx)

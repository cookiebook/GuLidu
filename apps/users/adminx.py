import xadmin
from users.models import BannerInfo, EmailVerifyCode
from xadmin import views


class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class CommXadminSetting(object):
    site_title = '谷粒教育后台管理系统'
    site_footer = '尚硅谷it教育'
    menu_style = 'accordion'        # 将菜单转换成折叠


class BannerInfoAdminx(object):
    list_display = ['image', 'url', 'add_time']
    list_search = ['image', 'url']
    list_filter = ['image', 'url']


class EmailVerifyCodeAdminx(object):
    list_display = ['code', 'email', 'send_type', 'add_time']


xadmin.site.register(BannerInfo, BannerInfoAdminx)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdminx)
# 注册主题类
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
# 系统名称
xadmin.site.register(views.CommAdminView, CommXadminSetting)
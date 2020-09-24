from users.models import EmailVerifyCode
from random import choice
from django.core.mail import send_mail
from GuLidu.settings import EMAIL_FROM

CODE_SIZE = 8


def get_randon_code(code_length):
    code_source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(code_length):
        code += choice(code_source)
    return code


def send_email_code(email, send_type):
    """
        第一步创建邮箱验证码，保存数据库，用来以后作对比
    """
    a = EmailVerifyCode()
    a.email = email
    a.send_type = send_type
    code = get_randon_code(CODE_SIZE)
    a.code = code
    a.save()
    if send_type == 1:
        send_title = '欢迎注册谷粒教育网站：'
        send_body = '请点击一下连接进行激活您的账号：\nhttp://127.0.0.1:8000/users/user_active/' + code
        result = send_mail(send_title, send_body, EMAIL_FROM, [email])
    elif send_type == 2:  # 发送修改密码的验证邮件
        send_title = '谷粒教育网站忘记密码：'
        send_body = '请点击一下连接修改您的账号密码：\nhttp://127.0.0.1:8000/users/user_reset/' + code
        result = send_mail(send_title, send_body, EMAIL_FROM, [email])
    else:  # 发送修改邮箱的验证邮件
        pass

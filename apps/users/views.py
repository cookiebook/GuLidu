from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm, UserLoginForm, UserForgetForm, UserResetForm
from .models import UserProfile, EmailVerifyCode
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from tools.send_mail_tool import send_email_code


def index(request):
    return render(request, 'users/index.html')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            email = user_login_form.cleaned_data['email']
            password = user_login_form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                if user.is_start:
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    return render(request, "users/login.html", {'msg': '该账户还未激活,请到邮件激活账户'})

            else:
                return render(request, "users/login.html", {'msg': '邮箱或者密码有误'})

        else:
            return render(request, 'users/login.html',
                          {'user_login_form': user_login_form})


def user_register(request):
    if request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request, 'users/register.html',
                      {'user_register_form': user_register_form})
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']
            user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user_list:
                return render(request, "users/register.html", {'msg': '该邮箱已经注册'})
            else:
                a = UserProfile()
                a.username = email
                a.email = email
                a.set_password(password)
                a.save()
                send_email_code(email, 1)  # 1表示注册邮件
                return redirect(reverse('users:user_login'))
        else:
            return render(request, 'users/register.html',
                          {'user_register_form': user_register_form})


def user_logout(request):
    logout(request)
    return redirect(reverse('index'))


def user_active(request, code):
    if code:
        email_ver_list = EmailVerifyCode.objects.filter(code=code)
        if email_ver_list:
            email_ver = email_ver_list[0]
            email = email_ver.email
            user_list = UserProfile.objects.filter(username=email)
            if user_list:
                user = user_list[0]
                user.is_start = True
                user.save()
                return redirect(reverse('users:user_login'))


def user_forget(request):
    if request.method == 'GET':
        user_forget_form = UserForgetForm()
        return render(request, 'users/forgetpwd.html',
                      {'user_forget_form': user_forget_form})
    else:
        user_forget_form = UserForgetForm(request.POST)
        if user_forget_form.is_valid():
            email = user_forget_form.cleaned_data['email']
            user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if not user_list:
                return render(request, "users/login.html", {'msg': '该用户不存在'})
            else:
                send_email_code(email, 2)  # 2表示修改密码邮件
                return redirect(reverse('users:user_login'))
        else:
            return render(request, 'users/forgetpwd.html',
                          {'user_forget_form': user_forget_form})


def user_reset(request, code):
    if request.method == 'GET':
        user_reset_form = UserResetForm()
        email_list = EmailVerifyCode.objects.filter(code=code)
        if not email_list:
            return render(request, "users/forgetpwd.html", {'msg': '验证码已失效'})
        else:
            return render(request, 'users/password_reset.html',
                          {'user_reset_form': user_reset_form, 'code': code})
    else:
        user_reset_form = UserResetForm(request.POST)
        if user_reset_form.is_valid():
            password = user_reset_form.cleaned_data['password']
            password1 = user_reset_form.cleaned_data['password1']
            if password == password1:
                email_list = EmailVerifyCode.objects.filter(code=code)
                if not email_list:
                    return render(request, "users/forgetpwd.html", {'msg': '验证码已失效'})
                else:
                    email = email_list[0]  # type: EmailVerifyCode
                    user_list = UserProfile.objects.filter(Q(username=email.email) | Q(email=email.email))
                    if user_list:
                        a = user_list[0]
                        a.set_password(password)
                        a.save()
                        return redirect(reverse('users:user_login'))
                    else:
                        return render(request, "users/forgetpwd.html", {'msg': '待修改密码用户已经不存在'})
            else:
                return render(request, 'users/password_reset.html',
                              {'user_reset_form': user_reset_form, 'code': code, 'msg': '两次密码不一致！'})
        else:
            return render(request, 'users/password_reset.html',
                          {'user_reset_form': user_reset_form, 'code': code})

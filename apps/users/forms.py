from django import forms
from captcha.fields import CaptchaField


class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=3, max_length=15, error_messages={
        'required': '密码必须填',
        'min_length': '密码最少3位',
        'max_length': '密码最多15位'})
    captcha = CaptchaField()


class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=3, max_length=15, error_messages={
        'required': '密码必须填',
        'min_length': '密码只是3位',
        'max_length': '密码最多15位'})


class UserForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()


class UserResetForm(forms.Form):
    password = forms.CharField(required=True, min_length=3, max_length=15, error_messages={
        'required': '密码必须填',
        'min_length': '密码最少3位',
        'max_length': '密码最多15位'})
    password1 = forms.CharField(required=True, min_length=3, max_length=15, error_messages={
        'required': '密码必须填',
        'min_length': '密码最少3位',
        'max_length': '密码最多15位'})

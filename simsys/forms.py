from django import forms
from django.core.exceptions import ValidationError

from simsys import models


class UserForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=25, label="用户名", error_messages={
        "min_length": "用户名不少于3个字符",
        "max_length": "用户名不超过25个字符",
        "required": "用户名不能为空"
    }, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'placeholder': '请输入您的用户名'
    }))
    password = forms.CharField(min_length=3, max_length=16, label='密码', error_messages={
        "min_length": "密码不少于3个字符",
        "max_length": "密码不超过25个字符",
        "required": "密码不能为空"
    }, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'autocomplete': 'off',
        'placeholder': '请输入您的密码'
    }))

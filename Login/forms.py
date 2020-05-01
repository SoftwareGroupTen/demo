from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class 自定义注册表单(UserCreationForm):
    昵称 = forms.CharField(required=False,max_length=50)
    身份 = forms.CharField(max_length=2)

    class Meta:
        model = User
        fields = ('username','password1','password2','email','昵称','身份')


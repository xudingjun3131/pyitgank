from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo

#定义登陆表单
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control uname', 'placeholder': '用户名', }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control pword m-b', 'placeholder': '密码', }))

#定义注册表单
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码', }))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码', }))
    class Meta:
        model = User
        fields = ("username", "email")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名', }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱地址', }),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords does not match.")
        return cd['password2']

#定义注册额外信息
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")
        widgets = {
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '请输入手机号码', }),
            'birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': '请输入出生日期', }),
        }

#定义用户中心
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme", "photo",)

#定义用户中心关联auth_user表类
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)


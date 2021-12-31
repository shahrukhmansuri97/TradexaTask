from django import forms
from .models import User, Post


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput()}
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'text']
        widgets = {'text': forms.Textarea()}
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username", "id":"username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"name@example.com", "id":"email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password", "id":"password1"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password again", "id":"password2"}))


    class Meta:
        model = User
        fields = ["username", "email"]
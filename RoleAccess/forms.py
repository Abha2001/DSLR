from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RoleAccessUser


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = RoleAccessUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

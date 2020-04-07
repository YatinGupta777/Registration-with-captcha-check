from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name','email','password']
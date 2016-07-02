from django import forms
from django.contrib.auth.models import User
from django.db import models


class LoginForm(forms.ModelForm):
    username_email = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ('username','password')


class SearchForm(forms.Form):
    search_bar_input = forms.CharField(max_length=64)
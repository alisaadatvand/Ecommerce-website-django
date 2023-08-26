from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Account
        fields =  ('username', 'first_name', 'last_name','email','phone_number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
         model = Account
         fields =  ('username', 'first_name', 'last_name','email','phone_number')

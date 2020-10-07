from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Regemp.models import ProfileMod


class ProfileFm(ModelForm):
    class Meta:
        model = ProfileMod
        fields = "__all__"
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'passwd': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

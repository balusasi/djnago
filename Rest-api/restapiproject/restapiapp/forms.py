from django import forms
from .models import loginmodel

class loginForm(forms.ModelForm):
    class Meta:
        model= loginmodel
        fields= ["username","password"]

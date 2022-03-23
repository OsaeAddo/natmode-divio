from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]


# Add CustomerForms

class CustomerForm(forms.ModelForm):
    class Meta: 
        model = models.Customer
        fields = [
            'mobile'
        ]
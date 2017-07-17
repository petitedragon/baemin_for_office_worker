from django import forms
#from django.forms import TextInput, Textarea, ModelForm
from django.forms import ModelForm
from .models import Partner, Menu

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = (
            "name",
            "contact",
            "address",
            "description",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "contact": forms.TextInput(attrs={"class":"form-control"}),
            "address": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
        }


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = (
            "image",
            "name",
            "price",
        )
        widgets = {
            #"image": TextInput(attrs={"class":"form-control"}),
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "price": forms.TextInput(attrs={"class":"form-control"}),
        }

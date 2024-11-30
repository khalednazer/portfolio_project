from django.forms import ModelForm
from .models import Por, Test
from django import forms
class form(ModelForm):
    class Meta:
        model= Por
        fields = '__all__' 
        widgets = {
            'tag':forms.CheckboxSelectMultiple(),
        }



class Ts(ModelForm):
    class Meta:
        model= Test
        fields = '__all__' 
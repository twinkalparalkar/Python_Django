
from django.forms import ModelForm
from django import forms

from .models import *

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model=Template
        fields='__all__'
        labels={'photo':''}

from django import forms
from .models import *

class CoffeeForm(forms.Form):
    coffee = forms.ModelChoiceField(queryset=Coffee.objects.all(), label="select the coffee")
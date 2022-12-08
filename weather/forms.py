from django.forms import ModelForm, TextInput
from django import forms

""" from .models import City """
""" 
class CityForm(ModelForm):
    city= forms.CharField(max_length=25)
    class Meta:
        model = City
        fields = ['name']
        widgets = { 'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Find your location...'}) } """
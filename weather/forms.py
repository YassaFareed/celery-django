from django import forms

class WeatherLocationForm(forms.Form):
    location = forms.CharField(label='Location', max_length='20')
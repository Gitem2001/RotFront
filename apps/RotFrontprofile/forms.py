from django import forms

from .models import RotFrontProfile

class RotFrontprofileForm(forms.ModelForm):
    class Meta:
        model = RotFrontProfile
        fields = ('avatar',)
from django import forms
from .models import support

class support(forms.ModelForm):
    class Meta:
        model = support
        fields = ['name', 'phone', 'email', 'program_participation', 'address']

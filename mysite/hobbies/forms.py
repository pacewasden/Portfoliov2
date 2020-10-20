from django import forms
from .models import Hobby

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['hobby_name', 'hobby_description', 'hobby_picture']
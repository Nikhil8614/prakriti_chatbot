from django import forms
from .models import AyurvedicBodyTest
class AyurvedicBodyTestForm(forms.ModelForm):
    class Meta:
        model = AyurvedicBodyTest
        fields = ['user_name', 'q1']





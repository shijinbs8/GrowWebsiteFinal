from django import forms
from .models import CallBackRequest

class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBackRequest
        fields = ['name', 'email', 'mobile', 'subject', 'message']
# forms.py
from django import forms


class MessageForm(forms.Form):
    content = forms.CharField(
        label='Message', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

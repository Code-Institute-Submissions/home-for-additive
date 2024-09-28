from .models import Prop
from django import forms


class NewProposal(forms.ModelForm):
    class Meta:
        model = Prop
        fields = ('title', 'keywords', 'email', 'content', 'supervisor')

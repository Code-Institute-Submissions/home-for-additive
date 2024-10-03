from .models import Prop, Assessment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewProposal(forms.ModelForm):
    class Meta:
        model = Prop
        fields = ('title', 'keywords', 'content')


class CommentOnProp(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ('content', 'approved')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Save the provided email
        if commit:
            user.save()
        return user

        

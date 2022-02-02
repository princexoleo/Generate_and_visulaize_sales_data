from django import forms
from .models import Profile

class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
from django import forms
from .models import PostT

class PostForm(forms.ModelForm):
    class Meta:
        model = PostT
        fields = ('title', 'text',)
        
from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    header = forms.CharField(min_length=5)

    class Meta:
       model = Post
       fields = [
           'header',
           'text',
           'author',
       ]

    def clean(self):
       cleaned_data = super().clean()
       header = cleaned_data.get("header")
       return cleaned_data

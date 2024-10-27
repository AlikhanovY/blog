from django import forms
from .models import Post, Comment
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
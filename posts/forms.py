from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    tags =forms.CharField(widget=forms.TextInput(attrs={'class': "input"}),label="Tags (Comma seperated)")

    class Meta:
        model = Post
        exclude = ("author","published_date","is_deleted","categories")
        widgets = {
            "title": forms.TextInput(attrs={'class': "input"}),
            "time_to_read": forms.TextInput(attrs={'class': "input"}),
            "short_description": forms.Textarea(attrs={'class': "input"}),
        }
        error_messages  = {
            "time_to_read": {
                "required": "Time Field is required"
            },
             "title": {
                "required": "Title Field is required"
            },
             "short_description": {
                "required": "Short description Field is required"
            },
             "description": {
                "required": "Description Field is required"
            },
        }
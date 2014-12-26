from django import forms
from datetime import datetime
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)

    def save(self, commit=True):
        self.instance.title = self.cleaned_data['title']
        self.instance.body = self.cleaned_data['body']
        if commit:
            self.instance.save()
        return self.instance

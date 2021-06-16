from ckeditor.widgets import CKEditorWidget
from django import forms

from main.models import Book


class CreateBookPostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Book
        fields = ['title', 'description', 'image', 'genre', 'tags']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateBookPostForm, self).__init__(*args, **kwargs)


    def save(self):
        data = self.cleaned_data
        data['author'] = self.request.user
        tags = data.pop('tags')
        post = Book.objects.create(**data)
        post.tags.add(*tags)
        return post


class UpdateBookPostForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'text', 'image', 'category', 'tags']
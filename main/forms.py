from ckeditor.widgets import CKEditorWidget
from django import forms

from main.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'published',
                  'image', 'genre', 'tags']


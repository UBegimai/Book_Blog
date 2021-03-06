

from django import forms

from .models import Book, Comment


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'published',
                  'image', 'genre', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name', 'comment_text')


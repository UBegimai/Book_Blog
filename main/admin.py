from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from django import forms

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Book
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Comment)

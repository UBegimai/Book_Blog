from django.contrib import admin

from main.models import Book, Genre, Author

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
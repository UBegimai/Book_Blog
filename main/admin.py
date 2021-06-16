from django.contrib import admin

from main.models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Comment)

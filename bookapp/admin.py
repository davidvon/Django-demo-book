__author__ = 'davidvon71'

from django.contrib import admin
from bookapp import models


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'title', 'author', 'translator', 'publisher', 'price',)
    list_filter = ('author', 'publisher',)
    search_fields = ('id', 'title', 'isbn',)
    list_per_page = 20


admin.site.register(models.Book, BookAdmin)

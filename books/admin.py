from django.contrib import admin
from .models import Category, Book


class BookInLine(admin.TabularInline):
    model = Book


class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInLine]


class BookAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    search_fields = ('title', 'author', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)

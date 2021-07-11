from django.contrib import admin

from .models import Author, Tag, Book, Borrow


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'slug')
    search_fields = ('slug',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cover', 'publication_date')
    list_filter = ('publication_date',)
    raw_id_fields = ('tags', 'authors')


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'borrow_date', 'returned_date', 'book')
    list_filter = ('user', 'borrow_date', 'returned_date', 'book')
from django.contrib import admin
from catalog.models import *


admin.site.register(MyModelName)
admin.site.register(Person)
admin.site.register(Language)
# admin.site.register(Genre)
# @admin.register(Genre)


# class InlineGenres(admin.TabularInline):
#     model = Books
#
# @admin.register(Genre)
# class AdminGenre(admin.ModelAdmin):
#     inlines = [InlineGenres]


admin.site.register(Status)

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_death', 'date_of_birth')]

@admin.register(BookInstance)
class AdminBookInstanse(admin.ModelAdmin):
    list_filter = ['book', 'status']
    fieldsets = (('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')}),
                 ('Статаус и окончание его действи', {'fields': ('status', 'due_back')}),)
    list_display = ['book', 'status', 'imprint']


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


# class BookStaceinstance(admin.StackedInline):
#     model = BookInstanse

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_authors', 'something')
    list_filter = ('title', 'language')
    inlines = [BookInstanceInline]
    # inlines = [BookStaceinstance]

class BookInlines(admin.TabularInline):
    model = Books

@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    inlines = [BookInlines]



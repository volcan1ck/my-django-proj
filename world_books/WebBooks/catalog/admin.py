from django.contrib import admin

from .models import Author, Book, Genre, Language, Status, BookInstance, Lecturer, Student, Course, Group
#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book)

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInLine]
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = [
        ('Book', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Status', {
            'fields': ('status', 'due_back')
        }),
    ]




admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Group)
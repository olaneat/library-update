from django.contrib import admin
from .models import Genre, Book, BookInstance, Language, Author

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
# Register your models here.
class AuthorInline(admin.TabularInline):
	model = Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'DOB', 'DOD')
	fields = ('first_name', 'last_name', 'DOB', 'DOD')
admin.site.register(Author,AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
	model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('tittle', 'author', 'display_genre')
	inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_date')

	fieldsets = 	(
		(None, {
			'fields': ('book', 'imprint', 'id')
			}),
		('Availability', {
			'fields': ('status', 'due_date')
			}),
		)
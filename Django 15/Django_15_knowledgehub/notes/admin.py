from django.contrib import admin

from notes.models import Category, Note, Tag


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',"slug")
    search_fields = ('name',"slug")
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content',  'author__username')
    list_filter = ('created_at', 'category')
    autocomplete_fields = ('author', 'category')
    filter_horizontal = ('tags',)

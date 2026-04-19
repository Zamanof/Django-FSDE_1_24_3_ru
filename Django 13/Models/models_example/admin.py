from django.contrib import admin
from .models import Notes
# Register your models here.

# admin.site.register(Notes)

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)
    list_filter = ('title',)


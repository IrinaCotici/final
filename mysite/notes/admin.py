from django.contrib import admin
# Register your models here.
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note
        field = '__all__'

admin.site.register(Note,NoteAdmin)
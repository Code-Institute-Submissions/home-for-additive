from django.contrib import admin
from .models import Prop
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Prop)
class PropAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'keywords',
        'student',
        'created_on',  # Removed 'status' and 'email'
    )
    search_fields = ['title', 'keywords', 'student__username']  # Search by student username, not the whole object
    list_filter = ('created_on',)  # Removed 'status'
    summernote_fields = ('content',)  # Keep this as it is for content editing

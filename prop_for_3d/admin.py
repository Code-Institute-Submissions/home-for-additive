from django.contrib import admin
from .models import Prop, Assessment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Prop)
class PropAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'keywords',
        'student',
        'created_on',
    )
    search_fields = ['title', 'keywords', 'student__username']
    list_filter = ('created_on',)
    summernote_fields = ('content',)
    

admin.site.register(Assessment)

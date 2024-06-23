from django.contrib import admin
from .models import Prop
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Prop)
class PropAdmin(SummernoteModelAdmin):

    list_display = (
        'title',
        'status',
        'keywords',
        'email',
        'student',
        'content',
        'created_on',)
    search_fields = ['title', 'keywords', 'student', ]
    list_filter = ('status', 'created_on',)
    summernote_fields = ('content',)

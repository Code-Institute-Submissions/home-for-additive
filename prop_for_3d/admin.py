from django.contrib import admin
from .models import Prop
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Prop)
class PropAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'keywords', 'email', 'student', 'created_on')
    search_fields = ['title', 'content', 'keywords']
    list_filter = ('status', 'created_on')    
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.




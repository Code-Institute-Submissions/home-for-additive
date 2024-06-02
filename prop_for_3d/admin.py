from django.contrib import admin
from .models import Prop, Assessment
from django_summernote.admin import SummernoteModelAdmin

class PropAdmin(SummernoteModelAdmin): # Or AssessmentAdmin? The most likely, PropAdmin...

    list_display = ('title', 'slug', 'status') # N.b. Slug is not in a model. May throw an error
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)} # N.b. Slug is not in a model. May throw an error. Can I comment out/delete this line?
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Prop)
admin.site.register(Assessment)



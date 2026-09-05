from django.contrib import admin 
from .models import Phones , Comment
# Register your models here.



class Phones_Admin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty'
    list_display  = ('name','memory','status','created_date')
    list_filter = ('status','name')
    search_fields = ['name','context']

admin.site.register(Phones,Phones_Admin)

class Comment_Admin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty'
    list_display  = ('post','author','is_approved','created_at')
    list_filter = ('author','message')
    search_fields = ['author','message']

admin.site.register(Comment,Comment_Admin)
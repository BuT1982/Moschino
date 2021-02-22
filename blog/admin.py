from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    save_as = True
    list_display = ('id', 'title', 'created_at', 'category')
    list_display_links = ('id', 'title')
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
from django.contrib import admin

# Register your models here.

from blogs.models import Author, Blog, BlogImage


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'education')
    search_fields = ('full_name',)
    list_filter = ('age',)
    ordering = ('full_name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'auther_id')
    search_fields = ('title', 'content')
    list_filter = ('date_added',)
    ordering = ('-date_added',)


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'blog_id')
    search_fields = ('blog_id__title',)
    list_filter = ('blog_id',)
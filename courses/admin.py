from django.contrib import admin

from courses.models import Course, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_of_students', 'price')
    search_fields = ('title', 'teachers')
    list_filter = ('duration', 'price')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'is_published', 'rating', 'course_id', 'blog_id', 'author_id')
    list_filter = ('is_published', 'rating')
    search_fields = ('name', 'email', 'comment')
    list_per_page = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(is_published=True)
        return qs
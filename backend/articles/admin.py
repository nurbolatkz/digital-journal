from django.contrib import admin
from .models import Article, Faculty, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "reviewer_name", "faculty", "category", "status", "published_at")
    list_filter = ("status", "category", "faculty")
    search_fields = ("title", "author_name", "reviewer_name", "summary", "annotation", "content", "resource_links")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)

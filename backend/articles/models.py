from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator


User = get_user_model()


class Faculty(models.Model):
    name = models.CharField(max_length=120, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLISHED = "published"
    STATUS_ARCHIVED = "archived"
    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    author_name = models.CharField(max_length=180, blank=True)
    reviewer_name = models.CharField(max_length=180, blank=True)
    publisher_name = models.CharField(max_length=180, blank=True, default="Kunaev University Press")
    publication_date = models.DateField(null=True, blank=True)
    doi = models.CharField(max_length=120, blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    annotation = models.TextField(blank=True)
    content = models.TextField()
    pdf_file = models.FileField(
        upload_to="articles/pdfs/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx"])],
    )
    pdf_url = models.URLField(blank=True)
    resource_links = models.TextField(blank=True, help_text="One URL per line")
    university = models.CharField(max_length=150, default="Kunaev University")
    faculty = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=80, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:250] or "article"
            slug = base_slug
            counter = 1
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        if self.status == self.STATUS_PUBLISHED:
            self.is_published = True
            if not self.published_at:
                from django.utils import timezone

                self.published_at = timezone.now()
        else:
            self.is_published = False
        super().save(*args, **kwargs)

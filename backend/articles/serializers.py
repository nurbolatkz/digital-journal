from django.conf import settings
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    pdf_document_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "author_name",
            "reviewer_name",
            "publisher_name",
            "publication_date",
            "doi",
            "keywords",
            "summary",
            "annotation",
            "content",
            "pdf_file",
            "pdf_document_url",
            "pdf_url",
            "resource_links",
            "university",
            "faculty",
            "category",
            "status",
            "is_published",
            "published_at",
            "created_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["slug", "created_by", "created_at", "updated_at"]

    def get_pdf_document_url(self, obj):
        if not obj.pdf_file:
            return ""
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(obj.pdf_file.url)
        return obj.pdf_file.url

    def validate_pdf_file(self, value):
        if not value:
            return value
        max_mb = getattr(settings, "ARTICLE_UPLOAD_MAX_MB", 10)
        max_bytes = int(max_mb) * 1024 * 1024
        if value.size > max_bytes:
            raise serializers.ValidationError(
                f"File is too large. Maximum allowed size is {max_mb} MB."
            )
        return value

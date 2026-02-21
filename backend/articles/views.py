from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article, Faculty, Category
from .serializers import ArticleSerializer


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class PublicArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    search_fields = ["title", "summary", "annotation", "content", "faculty", "category", "university"]
    ordering_fields = ["published_at", "created_at", "title"]
    ordering = ["-published_at"]

    def get_queryset(self):
        queryset = Article.objects.filter(status=Article.STATUS_PUBLISHED)
        category = self.request.query_params.get("category")
        faculty = self.request.query_params.get("faculty")
        if category:
            queryset = queryset.filter(category__iexact=category.strip())
        if faculty:
            queryset = queryset.filter(faculty__iexact=faculty.strip())
        return queryset


class PublicArticleDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    queryset = Article.objects.filter(status=Article.STATUS_PUBLISHED)


class ModeratorArticleListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsModerator]
    search_fields = ["title", "summary", "annotation", "content", "faculty", "category", "resource_links"]
    ordering_fields = ["published_at", "created_at", "updated_at", "title"]
    ordering = ["-updated_at"]
    queryset = Article.objects.all()
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ModeratorArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsModerator]
    queryset = Article.objects.all()
    lookup_field = "id"
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class ChangeArticleStatusView(APIView):
    permission_classes = [IsModerator]

    def post(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return Response({"detail": "Article not found."}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get("status")
        valid_statuses = {
            Article.STATUS_DRAFT,
            Article.STATUS_PUBLISHED,
            Article.STATUS_ARCHIVED,
        }
        if new_status not in valid_statuses:
            return Response(
                {"detail": "Invalid status. Use draft, published, or archived."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        article.status = new_status
        article.save()

        return Response(ArticleSerializer(article).data, status=status.HTTP_200_OK)


class ArticleFilterOptionsView(APIView):
    def get(self, request):
        published = Article.objects.filter(status=Article.STATUS_PUBLISHED)
        categories = sorted({value.strip() for value in published.values_list("category", flat=True) if value.strip()})
        faculties = sorted({value.strip() for value in published.values_list("faculty", flat=True) if value.strip()})
        return Response({"categories": categories, "faculties": faculties}, status=status.HTTP_200_OK)


class ModeratorTaxonomyOptionsView(APIView):
    permission_classes = [IsModerator]

    def get(self, request):
        categories = list(Category.objects.filter(is_active=True).values_list("name", flat=True))
        faculties = list(Faculty.objects.filter(is_active=True).values_list("name", flat=True))
        return Response({"categories": categories, "faculties": faculties}, status=status.HTTP_200_OK)

from django.urls import path
from .views import (
    PublicArticleListView,
    PublicArticleDetailView,
    ModeratorArticleListCreateView,
    ModeratorArticleDetailView,
    ChangeArticleStatusView,
    ArticleFilterOptionsView,
    ModeratorTaxonomyOptionsView,
)


urlpatterns = [
    path("articles/", PublicArticleListView.as_view(), name="public-article-list"),
    path("articles/filters/", ArticleFilterOptionsView.as_view(), name="public-article-filter-options"),
    path("articles/<slug:slug>/", PublicArticleDetailView.as_view(), name="public-article-detail"),
    path("moderator/articles/", ModeratorArticleListCreateView.as_view(), name="moderator-article-list-create"),
    path("moderator/options/", ModeratorTaxonomyOptionsView.as_view(), name="moderator-options"),
    path("moderator/articles/<int:id>/", ModeratorArticleDetailView.as_view(), name="moderator-article-detail"),
    path("moderator/articles/<int:article_id>/status/", ChangeArticleStatusView.as_view(), name="moderator-article-status"),
]

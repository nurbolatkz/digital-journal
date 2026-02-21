from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, max_length=280, unique=True)),
                ("summary", models.TextField(blank=True)),
                ("content", models.TextField()),
                ("university", models.CharField(default="Kunaev University", max_length=150)),
                ("faculty", models.CharField(blank=True, max_length=120)),
                ("category", models.CharField(blank=True, max_length=80)),
                ("is_published", models.BooleanField(default=False)),
                ("published_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="articles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-published_at", "-created_at"]},
        ),
    ]

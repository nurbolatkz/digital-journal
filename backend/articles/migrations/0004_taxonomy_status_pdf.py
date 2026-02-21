from django.db import migrations, models


def backfill_status_and_taxonomy(apps, schema_editor):
    Article = apps.get_model("articles", "Article")
    Faculty = apps.get_model("articles", "Faculty")
    Category = apps.get_model("articles", "Category")

    for article in Article.objects.all():
        if article.is_published:
            article.status = "published"
        else:
            article.status = "draft"
        article.save(update_fields=["status"])

        if article.faculty:
            Faculty.objects.get_or_create(name=article.faculty.strip())
        if article.category:
            Category.objects.get_or_create(name=article.category.strip())


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_article_publication_meta"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80, unique=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, unique=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.AddField(
            model_name="article",
            name="pdf_file",
            field=models.FileField(blank=True, null=True, upload_to="articles/pdfs/"),
        ),
        migrations.AddField(
            model_name="article",
            name="status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("published", "Published"), ("archived", "Archived")],
                default="draft",
                max_length=20,
            ),
        ),
        migrations.RunPython(backfill_status_and_taxonomy, migrations.RunPython.noop),
    ]

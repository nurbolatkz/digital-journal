from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_article_journal_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="author_name",
            field=models.CharField(blank=True, max_length=180),
        ),
        migrations.AddField(
            model_name="article",
            name="doi",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="article",
            name="keywords",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="article",
            name="publication_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="publisher_name",
            field=models.CharField(blank=True, default="Vuz Kunaeva University Press", max_length=180),
        ),
        migrations.AddField(
            model_name="article",
            name="reviewer_name",
            field=models.CharField(blank=True, max_length=180),
        ),
    ]

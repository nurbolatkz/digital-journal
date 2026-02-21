from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0005_alter_article_pdf_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="publisher_name",
            field=models.CharField(blank=True, default="Kunaev University Press", max_length=180),
        ),
    ]

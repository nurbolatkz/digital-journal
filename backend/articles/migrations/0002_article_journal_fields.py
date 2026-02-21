from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="annotation",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="article",
            name="pdf_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="article",
            name="resource_links",
            field=models.TextField(blank=True, help_text="One URL per line"),
        ),
    ]

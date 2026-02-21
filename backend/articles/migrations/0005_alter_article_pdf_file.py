from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0004_taxonomy_status_pdf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="pdf_file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="articles/pdfs/",
                validators=[django.core.validators.FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx"])],
            ),
        ),
    ]

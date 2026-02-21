from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from articles.models import Article, Faculty, Category


class Command(BaseCommand):
    help = "Create 3 sample published articles for backend integration check."

    def handle(self, *args, **options):
        user_model = get_user_model()
        moderator = user_model.objects.filter(is_staff=True).first()
        if not moderator:
            moderator = user_model.objects.create_user(
                username="moderator",
                password="Moderator123!",
                is_staff=True,
                is_superuser=True,
            )
            self.stdout.write(
                self.style.WARNING(
                    "Created moderator user: username=moderator, password=Moderator123!"
                )
            )

        samples = [
            {
                "title": "Digital Transformation in University Education",
                "author_name": "A. Sarsenbayev",
                "reviewer_name": "D. Ilyasov",
                "publisher_name": "Kunaev University Press",
                "publication_date": "2026-01-15",
                "doi": "10.2026/vkue.001",
                "keywords": "digitalization, lms, education",
                "summary": "Overview of LMS, digital libraries, and hybrid learning implementation.",
                "annotation": "The article analyzes key digital transformation steps and impact on quality.",
                "content": (
                    "The university is implementing digital services for students and faculty. "
                    "The outcomes include better access to materials, faster communication, and richer analytics."
                ),
                "pdf_url": "https://example.com/journal/digital-transformation.pdf",
                "resource_links": "https://vuzkunaeva.kz/\nhttps://example.com/lms-case-study",
                "faculty": "IT and Engineering",
                "category": "Education Technology",
                "status": "published",
                "university": "Kunaev University",
            },
            {
                "title": "Role of Student Research Clubs in Legal Studies",
                "author_name": "B. Nurgaliyeva",
                "reviewer_name": "T. Akhmetov",
                "publisher_name": "Kunaev University Press",
                "publication_date": "2026-01-22",
                "doi": "10.2026/vkue.002",
                "keywords": "law, student science, clubs",
                "summary": "How legal faculty research clubs improve student academic culture.",
                "annotation": "Institutional mechanisms for growing student research activity are discussed.",
                "content": (
                    "Research clubs help students develop legal analysis skills, improve academic writing, "
                    "and prepare for conference participation."
                ),
                "pdf_url": "https://example.com/journal/legal-research-clubs.pdf",
                "resource_links": "https://example.com/legal-methodology\nhttps://example.com/academic-writing",
                "faculty": "Law",
                "category": "Research",
                "status": "published",
                "university": "Kunaev University",
            },
            {
                "title": "Student Well-Being and Campus Support Services: 2026 Review",
                "author_name": "M. Williams",
                "reviewer_name": "R. Kassymov",
                "publisher_name": "Kunaev University Press",
                "publication_date": "2026-02-02",
                "doi": "10.2026/vkue.003",
                "keywords": "well-being, support services, retention",
                "summary": "A practical review of student support services and outcomes across the academic year.",
                "annotation": "The article evaluates counseling, mentoring, and career support service metrics.",
                "content": (
                    "The review highlights positive trends in student participation and retention where "
                    "integrated support models were implemented. Recommendations include proactive advising "
                    "and expanded peer mentoring."
                ),
                "pdf_url": "https://example.com/journal/student-wellbeing-2026.pdf",
                "resource_links": "https://example.com/student-support\nhttps://example.com/retention-study",
                "faculty": "Social Sciences",
                "category": "Campus Life",
                "status": "published",
                "university": "Kunaev University",
            },
        ]

        for sample in samples:
            if sample.get("faculty"):
                Faculty.objects.get_or_create(name=sample["faculty"])
            if sample.get("category"):
                Category.objects.get_or_create(name=sample["category"])

        created_count = 0
        for sample in samples:
            article, created = Article.objects.get_or_create(
                title=sample["title"],
                defaults={
                    **sample,
                    "created_by": moderator,
                    "is_published": True,
                    "published_at": timezone.now(),
                },
            )
            if not created:
                for field, value in sample.items():
                    setattr(article, field, value)
                article.is_published = True
                if not article.published_at:
                    article.published_at = timezone.now()
                article.created_by = moderator
                article.save()
            else:
                created_count += 1

        total_published = Article.objects.filter(is_published=True).count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Sample articles ready. Created: {created_count}. Total published: {total_published}."
            )
        )

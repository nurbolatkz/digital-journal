import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from articles.models import Article, Faculty, Category
from django.utils import timezone
from datetime import date

admin = User.objects.get(username='admin')

# Create Faculties
for f in ["Faculty of Law", "Faculty of Economics and Business", "Faculty of Information Technology", "Faculty of International Relations", "Faculty of Pedagogy and Psychology"]:
    Faculty.objects.get_or_create(name=f)

# Create Categories
for c in ["Research Article", "Review Article", "Case Study", "Conference Paper", "Methodology"]:
    Category.objects.get_or_create(name=c)

articles = [
    {
        "title": "Constitutional Reforms in Kazakhstan: A Comprehensive Analysis of 2022-2024 Amendments",
        "author_name": "Prof. Aibek Nurzhanov, Dr. Gulnara Suleimenova",
        "reviewer_name": "Prof. Marat Tazhin, Academy of Law",
        "publisher_name": "Kunaev University Press",
        "publication_date": date(2024, 11, 15),
        "doi": "10.5281/kunaev.2024.law.001",
        "keywords": "constitutional law, legal reforms, Kazakhstan, democratic transition, human rights",
        "summary": "This comprehensive study examines the constitutional amendments implemented in Kazakhstan between 2022 and 2024, analyzing their impact on the separation of powers and democratic governance.",
        "annotation": "The article presents a detailed legal analysis of Kazakhstan's constitutional reform process, drawing comparisons with international best practices.",
        "content": """Introduction\n\nThe constitutional reforms undertaken in Kazakhstan since 2022 represent one of the most significant transformations in the country's legal and political landscape since independence.\n\nKey Findings\n\n1. Redistribution of Presidential Powers - The amendments introduced significant limitations on presidential authority.\n\n2. Strengthening of Parliamentary Oversight - New mechanisms for legislative oversight have been established.\n\n3. Human Rights Protections - Constitutional amendments have expanded fundamental rights protections.\n\n4. Judicial Independence - Reforms to the appointment and tenure of judges aim to strengthen judicial independence.\n\nConclusion\n\nKazakhstan's constitutional reforms demonstrate a commitment to modernizing governance structures while maintaining stability.""",
        "faculty": "Faculty of Law",
        "category": "Research Article",
        "status": "published",
    },
    {
        "title": "Digital Transformation of Banking Sector in Central Asia: Challenges and Opportunities",
        "author_name": "Dr. Aigerim Bektursynova, Daniyar Ospanov MBA",
        "reviewer_name": "Prof. Kairat Kelimbetov, AIFC Academy",
        "publisher_name": "Kunaev University Press",
        "publication_date": date(2024, 10, 20),
        "doi": "10.5281/kunaev.2024.econ.002",
        "keywords": "digital banking, fintech, Central Asia, financial inclusion, blockchain, mobile payments",
        "summary": "This study examines the digital transformation processes in the banking sectors of Central Asian countries, with focus on Kazakhstan's experience as a regional leader.",
        "annotation": "The research provides empirical evidence on factors driving digital banking adoption in emerging markets.",
        "content": """Abstract\n\nThe banking sector in Central Asia is undergoing rapid digital transformation. This paper analyzes current state of digital banking development in the region.\n\nRegional Overview\n\nKazakhstan leads the region with mobile banking penetration reaching 67% of adult population by 2024. The AIFC has created favorable regulatory environment for fintech innovation.\n\nKey Technologies\n\n- Mobile Banking Platforms with improved functionality and security\n- Blockchain Applications for cross-border payments\n- AI-powered credit scoring systems\n\nChallenges\n\n- Cybersecurity threats\n- Digital literacy gaps\n- Infrastructure limitations\n\nConclusions\n\nDigital transformation presents significant opportunities for financial inclusion and economic development.""",
        "faculty": "Faculty of Economics and Business",
        "category": "Research Article",
        "status": "published",
    },
    {
        "title": "Machine Learning Approaches for Predicting Crop Yields in Semi-Arid Regions of Kazakhstan",
        "author_name": "Dr. Ruslan Kaliyev, Assem Nurgaziyeva MSc, Timur Kenzhebekov",
        "reviewer_name": "Prof. Serik Rakhimov, Nazarbayev University",
        "publisher_name": "Kunaev University Press",
        "publication_date": date(2024, 9, 5),
        "doi": "10.5281/kunaev.2024.it.003",
        "keywords": "machine learning, crop yield prediction, agriculture, Kazakhstan, random forest, neural networks",
        "summary": "This research presents novel machine learning models for predicting wheat and barley yields in Kazakhstan's semi-arid agricultural regions.",
        "annotation": "The study combines satellite imagery analysis, climate data, and soil characteristics to develop predictive models.",
        "content": """1. Introduction\n\nAgriculture remains vital to Kazakhstan's economy, contributing 5% to GDP and employing over 15% of workforce. Accurate crop yield prediction is essential for food security planning.\n\n2. Methodology\n\nFour machine learning approaches were evaluated:\n- Random Forest (RF)\n- Gradient Boosting (XGBoost)\n- LSTM Networks\n- Ensemble methods\n\n3. Results\n\nThe ensemble approach achieved best performance:\n- RMSE: 0.31 t/ha\n- MAPE: 8.7%\n- R-squared: 0.87\n\n4. Conclusions\n\nMachine learning offers valuable tools for agricultural planning in Kazakhstan.""",
        "faculty": "Faculty of Information Technology",
        "category": "Research Article",
        "status": "published",
    },
    {
        "title": "Belt and Road Initiative: Implications for Kazakhstan's Strategic Positioning",
        "author_name": "Dr. Zhanar Temirbekova, Yerzhan Aitkazin",
        "reviewer_name": "Prof. Bulat Sultanov, KAZISS",
        "publisher_name": "Kunaev University Press",
        "publication_date": date(2024, 8, 12),
        "doi": "10.5281/kunaev.2024.ir.004",
        "keywords": "Belt and Road Initiative, Kazakhstan, Eurasia, trade corridors, geopolitics, infrastructure",
        "summary": "This paper analyzes Kazakhstan's evolving role in China's Belt and Road Initiative as a key transit hub in Eurasian connectivity.",
        "annotation": "Drawing on trade data and policy documents, the study provides balanced assessment of BRI's impact on Kazakhstan.",
        "content": """Introduction\n\nSince 2013, China's Belt and Road Initiative has become one of the most ambitious infrastructure projects in history. Kazakhstan occupies a unique position in this strategy.\n\nEconomic Impact\n\nKazakhstan-China trade growth:\n- 2013: $28.6 billion\n- 2023: $41.2 billion\n\nMajor projects include Khorgos Gateway and the Western Europe-Western China highway.\n\nStrategic Considerations\n\nKazakhstan maintains multi-vector foreign policy while engaging with BRI, balancing relationships with China, Russia, and the West.\n\nConclusions\n\nKazakhstan has successfully leveraged its strategic location to benefit from BRI while maintaining policy independence.""",
        "faculty": "Faculty of International Relations",
        "category": "Research Article",
        "status": "published",
    },
    {
        "title": "Innovative Approaches to Trilingual Education in Kazakhstan: A Longitudinal Study",
        "author_name": "Prof. Maira Kozhabekova, Dr. Saule Karabayeva",
        "reviewer_name": "Prof. Kulyash Shamshidinova, NIS",
        "publisher_name": "Kunaev University Press",
        "publication_date": date(2024, 7, 25),
        "doi": "10.5281/kunaev.2024.edu.005",
        "keywords": "trilingual education, Kazakhstan, language policy, CLIL, educational reform",
        "summary": "This five-year study evaluates implementation and outcomes of Kazakhstan's trilingual education policy.",
        "annotation": "The research provides evidence-based recommendations for improving trilingual education delivery.",
        "content": """Abstract\n\nKazakhstan's trilingual education policy represents an ambitious educational reform. This study tracks implementation from 2019 to 2024.\n\nFindings\n\nStudent Achievement:\n- Mathematics: No significant difference between English and Russian instruction\n- Biology: Initial challenges in English, improving over time\n- English proficiency gains exceeding comparison groups\n\nTeacher Factors\n\nTeacher English proficiency and pedagogical training emerged as critical success factors.\n\nRecommendations\n\n1. Extended teacher training programs\n2. Development of localized teaching materials\n3. Flexible implementation timelines\n4. Increased investment in rural education""",
        "faculty": "Faculty of Pedagogy and Psychology",
        "category": "Research Article",
        "status": "published",
    },
    {
        "title": "Comparative Analysis of Civil Law Codification: Kazakhstan, Germany, and France",
        "author_name": "Dr. Baurzhan Mukhamedzhanov",
        "reviewer_name": "Prof. Serikbay Baimoldayev, Caspian University",
        "publisher_name": "Kunaev University Press",
        "publication_date": date(2024, 6, 18),
        "doi": "10.5281/kunaev.2024.law.006",
        "keywords": "civil law, codification, comparative law, Kazakhstan, Germany, France",
        "summary": "This comparative study examines structure and principles of civil law codification in Kazakhstan.",
        "annotation": "The article provides insights for understanding Kazakhstan's Civil Code within European legal traditions.",
        "content": """Introduction\n\nKazakhstan's Civil Code represents a significant achievement in post-Soviet legal development.\n\nThe French Model\n\nThe Napoleonic Code established the paradigm:\n- Comprehensive coverage of private law\n- Systematic organization\n- Balance of individual rights and social obligations\n\nThe German Model\n\nThe BGB introduced:\n- Abstract general concepts\n- Hierarchical structure\n- Scientific legal methodology\n\nKazakhstan's Approach\n\nCombines elements from both traditions while adapting to local context.\n\nConclusions\n\nKazakhstan's civil codification demonstrates successful legal development through selective borrowing and creative adaptation.""",
        "faculty": "Faculty of Law",
        "category": "Review Article",
        "status": "published",
    },
    {
        "title": "Sustainable Urban Development in Astana: Green Building Practices",
        "author_name": "Dr. Nurlan Bekturganov, Assel Yermekova MSc",
        "reviewer_name": "Prof. Kanat Baigarin, Satbayev University",
        "publisher_name": "Kunaev University Press",
        "publication_date": date(2024, 5, 30),
        "doi": "10.5281/kunaev.2024.env.007",
        "keywords": "sustainable development, green building, Astana, urban planning, energy efficiency",
        "summary": "This research analyzes implementation of green building practices in Astana.",
        "annotation": "The study provides recommendations for accelerating sustainable urban development.",
        "content": """Executive Summary\n\nAstana has emerged as a testing ground for sustainable urban development in Central Asia.\n\nGreen Building Certification\n\n- LEED certified buildings: 12\n- BREEAM certified: 5\n- Local standards: 45\n\nPerformance Outcomes\n\n- Energy savings: 25-40% compared to conventional construction\n- Water conservation: 30-50% reduction\n- Favorable lifecycle economics\n\nChallenges\n\n- Extreme climate (-40°C to +40°C)\n- Limited local expertise\n- Material import dependency\n\nRecommendations\n\n1. Strengthen building energy codes\n2. Expand incentive programs\n3. Develop local certification systems""",
        "faculty": "Faculty of Economics and Business",
        "category": "Case Study",
        "status": "published",
    },
    {
        "title": "Cybersecurity Challenges in Kazakhstan's Critical Infrastructure",
        "author_name": "Dr. Marat Smaguliev, Almas Bekmuratov PhD",
        "reviewer_name": "Prof. Darkhan Nurpeisov, KazNU",
        "publisher_name": "Kunaev University Press",
        "publication_date": date(2024, 4, 10),
        "doi": "10.5281/kunaev.2024.it.008",
        "keywords": "cybersecurity, critical infrastructure, risk assessment, Kazakhstan, SCADA",
        "summary": "This paper develops a comprehensive cybersecurity risk assessment framework for Kazakhstan's critical infrastructure.",
        "annotation": "The framework provides practical tools for evaluating and improving cybersecurity posture.",
        "content": """Abstract\n\nAs Kazakhstan accelerates digital transformation of critical infrastructure, cybersecurity risks have become a national priority.\n\nCritical Sectors\n\n- Energy (oil, gas, electricity)\n- Transportation\n- Communications\n- Financial services\n- Government services\n\nThreat Landscape\n\n- Nation-state actors\n- Cybercriminal organizations\n- Insider threats\n\nRisk Assessment Framework\n\nRisk = Likelihood × Impact × Vulnerability\n\nHigh-Risk Areas\n\n- Legacy industrial control systems\n- Insufficient network segmentation\n- Third-party vendor risks\n\nRecommendations\n\n1. Implement network segmentation\n2. Deploy continuous monitoring\n3. Establish security operations centers\n4. Regular penetration testing""",
        "faculty": "Faculty of Information Technology",
        "category": "Research Article",
        "status": "published",
    },
]

for data in articles:
    Article.objects.create(
        created_by=admin,
        is_published=True,
        published_at=timezone.now(),
        university="Kunaev University",
        **data
    )
    print(f"Created: {data['title'][:50]}...")

print(f"\nTotal articles: {Article.objects.count()}")

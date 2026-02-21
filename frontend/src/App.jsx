import { useEffect, useState } from "react";
import { Link, NavLink, Navigate, Route, Routes, useLocation, useNavigate } from "react-router-dom";
import {
  createArticle,
  changeArticleStatus,
  fetchFilterOptions,
  fetchModeratorOptions,
  fetchModeratorArticles,
  fetchPublicArticle,
  fetchPublicArticles,
  moderatorLogin
} from "./api";

const translations = {
  en: {
    journalName: "Kunaev University Digital Journal",
    mainSite: "Main website",
    brandSub: "Official Article Publishing Platform",
    navArticles: "Articles",
    navDashboard: "Dashboard",
    navLogin: "Login",
    heroKicker: "Academic Communications",
    heroTitle: "University News, Research, and Student Life",
    heroText:
      "Explore official publications from faculties and departments. Articles are reviewed and published by the university moderator.",
    findPublications: "Find Publications",
    searchHint: "Search by keyword, category, and faculty.",
    searchInput: "Search title/content...",
    allCategories: "All categories",
    allFaculties: "All faculties",
    publishedArticles: "Published University Articles",
    items: "items",
    loading: "Loading...",
    noSummary: "No summary provided.",
    generalFaculty: "General faculty",
    noArticles: "No published articles found.",
    universityLabel: "University",
    publicationInfo: "Publication Information",
    author: "Author",
    reviewer: "Reviewer",
    publisher: "Publisher",
    publicationDate: "Publication date",
    doi: "DOI",
    keywords: "Keywords",
    annotation: "Annotation",
    pdfFile: "PDF File",
    openPdf: "Open PDF publication",
    references: "References and External Links",
    fullArticle: "Full Article",
    moderatorLogin: "Moderator Login",
    username: "Username",
    password: "Password",
    login: "Login",
    moderatorDashboard: "Moderator Dashboard",
    logout: "Logout",
    createArticle: "Create New Article",
    articleTitle: "Article title",
    summary: "Summary / abstract",
    content: "Content",
    pdfUrl: "PDF URL (https://...)",
    refsPerLine: "Reference links (one URL per line)",
    chooseFaculty: "Select faculty",
    chooseCategory: "Select category",
    uploadPdf: "Upload file (PDF/DOC/DOCX)",
    status: "Status",
    statusDraft: "Draft",
    statusPublished: "Published",
    statusArchived: "Archived",
    setStatus: "Set status",
    faculty: "Faculty",
    category: "Category",
    saveDraft: "Save Draft",
    existingArticles: "Existing Articles",
    published: "Published",
    draft: "Draft",
    pdfAttached: "PDF attached",
    noPdf: "No PDF file",
    publish: "Publish",
    rights: "All rights reserved.",
    invalidCredentials: "Invalid credentials"
  },
  ru: {
    journalName: "Цифровой журнал Университета Кунаева",
    mainSite: "Основной сайт",
    brandSub: "Официальная платформа публикации статей",
    navArticles: "Статьи",
    navDashboard: "Панель",
    navLogin: "Вход",
    heroKicker: "Академические коммуникации",
    heroTitle: "Новости университета, исследования и студенческая жизнь",
    heroText:
      "Изучайте официальные публикации факультетов и подразделений. Статьи проверяются и публикуются модератором университета.",
    findPublications: "Поиск публикаций",
    searchHint: "Поиск по ключевым словам, категориям и факультетам.",
    searchInput: "Поиск по заголовку/тексту...",
    allCategories: "Все категории",
    allFaculties: "Все факультеты",
    publishedArticles: "Опубликованные статьи университета",
    items: "материалов",
    loading: "Загрузка...",
    noSummary: "Краткое описание отсутствует.",
    generalFaculty: "Общий факультет",
    noArticles: "Опубликованные статьи не найдены.",
    universityLabel: "Университет",
    publicationInfo: "Сведения о публикации",
    author: "Автор",
    reviewer: "Рецензент",
    publisher: "Издатель",
    publicationDate: "Дата публикации",
    doi: "DOI",
    keywords: "Ключевые слова",
    annotation: "Аннотация",
    pdfFile: "PDF файл",
    openPdf: "Открыть PDF публикацию",
    references: "Ссылки и внешние материалы",
    fullArticle: "Полный текст статьи",
    moderatorLogin: "Вход модератора",
    username: "Логин",
    password: "Пароль",
    login: "Войти",
    moderatorDashboard: "Панель модератора",
    logout: "Выйти",
    createArticle: "Создать новую статью",
    articleTitle: "Название статьи",
    summary: "Краткое описание / абстракт",
    content: "Содержание",
    pdfUrl: "Ссылка на PDF (https://...)",
    refsPerLine: "Ссылки на источники (по одной в строке)",
    chooseFaculty: "Выберите факультет",
    chooseCategory: "Выберите категорию",
    uploadPdf: "Загрузить файл (PDF/DOC/DOCX)",
    status: "Статус",
    statusDraft: "Черновик",
    statusPublished: "Опубликовано",
    statusArchived: "Архив",
    setStatus: "Обновить статус",
    faculty: "Факультет",
    category: "Категория",
    saveDraft: "Сохранить черновик",
    existingArticles: "Существующие статьи",
    published: "Опубликовано",
    draft: "Черновик",
    pdfAttached: "PDF прикреплен",
    noPdf: "PDF отсутствует",
    publish: "Опубликовать",
    rights: "Все права защищены.",
    invalidCredentials: "Неверные учетные данные"
  },
  kz: {
    journalName: "Қонаев университетінің цифрлық журналы",
    mainSite: "Негізгі сайт",
    brandSub: "Мақала жариялаудың ресми платформасы",
    navArticles: "Мақалалар",
    navDashboard: "Панель",
    navLogin: "Кіру",
    heroKicker: "Академиялық коммуникациялар",
    heroTitle: "Университет жаңалықтары, зерттеулер және студенттік өмір",
    heroText:
      "Факультеттер мен бөлімдердің ресми жарияланымдарын қараңыз. Мақалалар университет модераторы арқылы тексеріліп жарияланады.",
    findPublications: "Жарияланым іздеу",
    searchHint: "Кілт сөз, санат және факультет бойынша іздеу.",
    searchInput: "Тақырып/мәтін бойынша іздеу...",
    allCategories: "Барлық санат",
    allFaculties: "Барлық факультет",
    publishedArticles: "Университеттің жарияланған мақалалары",
    items: "материал",
    loading: "Жүктелуде...",
    noSummary: "Қысқаша сипаттама жоқ.",
    generalFaculty: "Жалпы факультет",
    noArticles: "Жарияланған мақалалар табылмады.",
    universityLabel: "Университет",
    publicationInfo: "Жарияланым туралы мәлімет",
    author: "Автор",
    reviewer: "Рецензент",
    publisher: "Баспагер",
    publicationDate: "Жарияланған күні",
    doi: "DOI",
    keywords: "Түйін сөздер",
    annotation: "Аннотация",
    pdfFile: "PDF файл",
    openPdf: "PDF жарияланымды ашу",
    references: "Сілтемелер және сыртқы материалдар",
    fullArticle: "Мақаланың толық мәтіні",
    moderatorLogin: "Модератор кіруі",
    username: "Логин",
    password: "Құпиясөз",
    login: "Кіру",
    moderatorDashboard: "Модератор панелі",
    logout: "Шығу",
    createArticle: "Жаңа мақала құру",
    articleTitle: "Мақала атауы",
    summary: "Қысқаша сипаттама / аннотация",
    content: "Мазмұны",
    pdfUrl: "PDF сілтемесі (https://...)",
    refsPerLine: "Дереккөз сілтемелері (әр жолға біреу)",
    chooseFaculty: "Факультетті таңдаңыз",
    chooseCategory: "Санатты таңдаңыз",
    uploadPdf: "Файл жүктеу (PDF/DOC/DOCX)",
    status: "Мәртебе",
    statusDraft: "Қаралым",
    statusPublished: "Жарияланған",
    statusArchived: "Мұрағат",
    setStatus: "Мәртебені орнату",
    faculty: "Факультет",
    category: "Санат",
    saveDraft: "Қаралымды сақтау",
    existingArticles: "Бар мақалалар",
    published: "Жарияланған",
    draft: "Қаралым",
    pdfAttached: "PDF тіркелген",
    noPdf: "PDF жоқ",
    publish: "Жариялау",
    rights: "Барлық құқықтар қорғалған.",
    invalidCredentials: "Жарамсыз тіркелгі деректері"
  }
};

function useAuth() {
  const [token, setToken] = useState(() => localStorage.getItem("moderator_token") || "");

  const login = (newToken) => {
    localStorage.setItem("moderator_token", newToken);
    setToken(newToken);
  };

  const logout = () => {
    localStorage.removeItem("moderator_token");
    setToken("");
  };

  return { token, isAuthenticated: Boolean(token), login, logout };
}

function Layout({ children, language, setLanguage, t, isAuthenticated, onLogout }) {
  const location = useLocation();
  const isHeroPage = location.pathname === "/" || location.pathname.startsWith("/article/");

  return (
    <div className="page">
      <div className="top-strip">
        <p>{t.journalName}</p>
        <div className="top-strip-right">
          <a href="https://vuzkunaeva.kz/" target="_blank" rel="noreferrer">
            {t.mainSite}: vuzkunaeva.kz
          </a>
          <div className="lang-switch">
            {["kz", "ru", "en"].map((lang) => (
              <button
                key={lang}
                type="button"
                className={language === lang ? "active" : ""}
                onClick={() => setLanguage(lang)}
              >
                {lang.toUpperCase()}
              </button>
            ))}
          </div>
        </div>
      </div>
      <header className="header">
        <div className="brand-wrap">
          <div className="brand-seal">KU</div>
          <div>
            <Link to="/" className="brand">
              Kunaev University
            </Link>
            <p className="brand-sub">{t.brandSub}</p>
          </div>
        </div>
        <nav className="nav">
          <NavLink to="/" className={({ isActive }) => (isActive ? "active" : "")}>{t.navArticles}</NavLink>
          {isAuthenticated ? (
            <>
              <NavLink to="/dashboard" className={({ isActive }) => (isActive ? "active" : "")}>{t.navDashboard}</NavLink>
              <button className="nav-logout" onClick={onLogout}>{t.logout}</button>
            </>
          ) : (
            <NavLink to="/login" className={({ isActive }) => (isActive ? "active" : "")}>{t.navLogin}</NavLink>
          )}
        </nav>
      </header>
      {isHeroPage && (
        <section className="hero">
          <p className="hero-kicker">{t.heroKicker}</p>
          <h1>{t.heroTitle}</h1>
          <p>{t.heroText}</p>
        </section>
      )}
      <main className="main-shell">{children}</main>
      <footer className="footer">2026 Kunaev University. {t.rights}</footer>
    </div>
  );
}

function PublicListPage({ t }) {
  const [articles, setArticles] = useState([]);
  const [filters, setFilters] = useState({ categories: [], faculties: [] });
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("");
  const [faculty, setFaculty] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchFilterOptions().then(setFilters).catch(() => setFilters({ categories: [], faculties: [] }));
  }, []);

  useEffect(() => {
    setLoading(true);
    setError("");
    fetchPublicArticles({ search, category, faculty })
      .then(setArticles)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [search, category, faculty]);

  return (
    <section className="content public-grid">
      <aside className="filter-panel">
        <h2>{t.findPublications}</h2>
        <p>{t.searchHint}</p>
        <div className="controls">
          <input placeholder={t.searchInput} value={search} onChange={(e) => setSearch(e.target.value)} />
          <select value={category} onChange={(e) => setCategory(e.target.value)}>
            <option value="">{t.allCategories}</option>
            {filters.categories.map((item) => (
              <option value={item} key={item}>{item}</option>
            ))}
          </select>
          <select value={faculty} onChange={(e) => setFaculty(e.target.value)}>
            <option value="">{t.allFaculties}</option>
            {filters.faculties.map((item) => (
              <option value={item} key={item}>{item}</option>
            ))}
          </select>
        </div>
      </aside>
      <div className="content-panel">
        <div className="section-head">
          <h2>{t.publishedArticles}</h2>
          <span>{articles.length} {t.items}</span>
        </div>
        <p className="section-intro">
          Official digital journal publications from faculties and research units.
        </p>
        {loading && <p>{t.loading}</p>}
        {error && <p className="error">{error}</p>}
        <div className="cards">
          {articles.map((article, index) => (
            <article className="card reveal-card" style={{ "--delay": `${index * 70}ms` }} key={article.id}>
              <p className="meta-chip">{article.category || t.universityLabel}</p>
              <h3><Link to={`/article/${article.slug}`}>{article.title}</Link></h3>
              <p>{article.summary || t.noSummary}</p>
              <p className="meta">{article.university} | {article.faculty || t.generalFaculty}</p>
            </article>
          ))}
        </div>
        {!loading && articles.length === 0 && <p>{t.noArticles}</p>}
      </div>
    </section>
  );
}

function PublicArticlePage({ t }) {
  const [article, setArticle] = useState(null);
  const [error, setError] = useState("");
  const slug = window.location.pathname.split("/article/")[1];

  useEffect(() => {
    fetchPublicArticle(slug).then(setArticle).catch((err) => setError(err.message));
  }, [slug]);

  if (error) return <p className="error">{error}</p>;
  if (!article) return <p>{t.loading}</p>;

  const resourceLinks = (article.resource_links || "").split("\n").map((item) => item.trim()).filter(Boolean);

  return (
    <article className="content article-view">
      <h1>{article.title}</h1>
      <p className="meta">{article.university} | {article.faculty || t.generalFaculty} | {article.category || t.universityLabel}</p>
      <section className="journal-block">
        <h3>{t.publicationInfo}</h3>
        <div className="meta-grid">
          <p><strong>{t.author}:</strong> {article.author_name || "-"}</p>
          <p><strong>{t.reviewer}:</strong> {article.reviewer_name || "-"}</p>
          <p><strong>{t.publisher}:</strong> {article.publisher_name || "-"}</p>
          <p><strong>{t.publicationDate}:</strong> {article.publication_date || "-"}</p>
          <p><strong>{t.doi}:</strong> {article.doi || "-"}</p>
          <p><strong>{t.keywords}:</strong> {article.keywords || "-"}</p>
        </div>
      </section>
      {article.annotation && <section className="journal-block"><h3>{t.annotation}</h3><p>{article.annotation}</p></section>}
      {article.summary && <p className="article-summary">{article.summary}</p>}
      {(article.pdf_document_url || article.pdf_url) && (
        <section className="journal-block">
          <h3>{t.pdfFile}</h3>
          <a href={article.pdf_document_url || article.pdf_url} target="_blank" rel="noreferrer" className="resource-link">{t.openPdf}</a>
        </section>
      )}
      {resourceLinks.length > 0 && (
        <section className="journal-block">
          <h3>{t.references}</h3>
          <ul className="resource-list">
            {resourceLinks.map((link) => (
              <li key={link}><a href={link} target="_blank" rel="noreferrer" className="resource-link">{link}</a></li>
            ))}
          </ul>
        </section>
      )}
      <section className="journal-block"><h3>{t.fullArticle}</h3><div className="article-body">{article.content}</div></section>
    </article>
  );
}

function LoginPage({ t, onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      const data = await moderatorLogin(username, password);
      onLogin(data.token);
      navigate("/dashboard");
    } catch {
      setError(t.invalidCredentials);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="content login-page">
      <h1>{t.moderatorLogin}</h1>
      <form onSubmit={handleSubmit} className="form panel login-form">
        <input
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder={t.username}
          required
          autoFocus
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder={t.password}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? t.loading : t.login}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
    </section>
  );
}

function DashboardPage({ t, token }) {
  const [articles, setArticles] = useState([]);
  const [options, setOptions] = useState({ faculties: [], categories: [] });
  const [statusUpdates, setStatusUpdates] = useState({});
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const [form, setForm] = useState({
    title: "",
    author_name: "",
    reviewer_name: "",
    publisher_name: "Kunaev University Press",
    publication_date: "",
    doi: "",
    keywords: "",
    summary: "",
    annotation: "",
    content: "",
    pdf_url: "",
    pdf_file: null,
    resource_links: "",
    university: "Kunaev University",
    faculty: "",
    category: ""
  });

  const loadArticles = () => {
    if (!token) return;
    fetchModeratorArticles(token).then(setArticles).catch((err) => setError(err.message));
  };

  const loadOptions = () => {
    if (!token) return;
    fetchModeratorOptions(token)
      .then(setOptions)
      .catch(() => setOptions({ faculties: [], categories: [] }));
  };

  useEffect(() => {
    loadArticles();
    loadOptions();
  }, [token]);

  const onCreate = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");
    try {
      await createArticle(token, form);
      setForm({
        title: "",
        author_name: "",
        reviewer_name: "",
        publisher_name: "Kunaev University Press",
        publication_date: "",
        doi: "",
        keywords: "",
        summary: "",
        annotation: "",
        content: "",
        pdf_url: "",
        pdf_file: null,
        resource_links: "",
        university: "Kunaev University",
        faculty: "",
        category: ""
      });
      loadArticles();
      loadOptions();
      setSuccess("Article created successfully!");
      setTimeout(() => setSuccess(""), 3000);
    } catch (err) {
      setError(err.message);
    }
  };

  const onStatusChange = async (id) => {
    const nextStatus = statusUpdates[id];
    if (!nextStatus) return;
    setError("");
    try {
      await changeArticleStatus(token, id, nextStatus);
      loadArticles();
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <section className="content">
      <div className="section-head">
        <h1>{t.moderatorDashboard}</h1>
      </div>

      {success && <p className="success">{success}</p>}
      {error && <p className="error">{error}</p>}

      <form onSubmit={onCreate} className="form panel">
        <h3>{t.createArticle}</h3>
        <div className="form-divider">Publication Metadata</div>
        <input value={form.title} onChange={(e) => setForm((prev) => ({ ...prev, title: e.target.value }))} placeholder={t.articleTitle} required />
        <input value={form.author_name} onChange={(e) => setForm((prev) => ({ ...prev, author_name: e.target.value }))} placeholder={t.author} />
        <input value={form.reviewer_name} onChange={(e) => setForm((prev) => ({ ...prev, reviewer_name: e.target.value }))} placeholder={t.reviewer} />
        <input value={form.publisher_name} onChange={(e) => setForm((prev) => ({ ...prev, publisher_name: e.target.value }))} placeholder={t.publisher} />
        <input type="date" value={form.publication_date} onChange={(e) => setForm((prev) => ({ ...prev, publication_date: e.target.value }))} placeholder={t.publicationDate} />
        <input value={form.doi} onChange={(e) => setForm((prev) => ({ ...prev, doi: e.target.value }))} placeholder={t.doi} />
        <input value={form.keywords} onChange={(e) => setForm((prev) => ({ ...prev, keywords: e.target.value }))} placeholder={t.keywords} />
        <div className="form-divider">Article Content</div>
        <input value={form.summary} onChange={(e) => setForm((prev) => ({ ...prev, summary: e.target.value }))} placeholder={t.summary} />
        <textarea value={form.annotation} onChange={(e) => setForm((prev) => ({ ...prev, annotation: e.target.value }))} placeholder={t.annotation} rows={4} />
        <textarea value={form.content} onChange={(e) => setForm((prev) => ({ ...prev, content: e.target.value }))} placeholder={t.content} rows={7} required />
        <label>{t.uploadPdf}</label>
        <input
          type="file"
          accept=".pdf,.doc,.docx,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
          onChange={(e) => setForm((prev) => ({ ...prev, pdf_file: e.target.files?.[0] || null }))}
        />
        <input type="url" value={form.pdf_url} onChange={(e) => setForm((prev) => ({ ...prev, pdf_url: e.target.value }))} placeholder={t.pdfUrl} />
        <textarea value={form.resource_links} onChange={(e) => setForm((prev) => ({ ...prev, resource_links: e.target.value }))} placeholder={t.refsPerLine} rows={4} />
        <input value={form.university} onChange={(e) => setForm((prev) => ({ ...prev, university: e.target.value }))} placeholder={t.universityLabel} />
        <select value={form.faculty} onChange={(e) => setForm((prev) => ({ ...prev, faculty: e.target.value }))}>
          <option value="">{t.chooseFaculty}</option>
          {options.faculties.map((item) => (
            <option key={item} value={item}>
              {item}
            </option>
          ))}
        </select>
        <select value={form.category} onChange={(e) => setForm((prev) => ({ ...prev, category: e.target.value }))}>
          <option value="">{t.chooseCategory}</option>
          {options.categories.map((item) => (
            <option key={item} value={item}>
              {item}
            </option>
          ))}
        </select>
        <button type="submit">{t.saveDraft}</button>
      </form>

      <h2>{t.existingArticles}</h2>
      <div className="cards">
        {articles.map((article) => (
          <article className="card status-card" key={article.id}>
            <p className="meta-chip">{article.status === "published" ? t.statusPublished : article.status === "archived" ? t.statusArchived : t.statusDraft}</p>
            <h3>{article.title}</h3>
            <p className="meta">{article.faculty || t.generalFaculty}</p>
            <p className="meta">{article.pdf_document_url || article.pdf_url ? t.pdfAttached : t.noPdf}</p>
            <select
              value={statusUpdates[article.id] || article.status || "draft"}
              onChange={(e) => setStatusUpdates((prev) => ({ ...prev, [article.id]: e.target.value }))}
            >
              <option value="draft">{t.statusDraft}</option>
              <option value="published">{t.statusPublished}</option>
              <option value="archived">{t.statusArchived}</option>
            </select>
            <button type="button" onClick={() => onStatusChange(article.id)}>
              {t.setStatus}
            </button>
          </article>
        ))}
      </div>
    </section>
  );
}

function ProtectedRoute({ children, isAuthenticated }) {
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }
  return children;
}

export default function App() {
  const [language, setLanguage] = useState(() => localStorage.getItem("journal_lang") || "kz");
  const { token, isAuthenticated, login, logout } = useAuth();

  useEffect(() => {
    localStorage.setItem("journal_lang", language);
  }, [language]);

  const t = translations[language] || translations.kz;

  return (
    <Layout language={language} setLanguage={setLanguage} t={t} isAuthenticated={isAuthenticated} onLogout={logout}>
      <Routes>
        <Route path="/" element={<PublicListPage t={t} />} />
        <Route path="/article/:slug" element={<PublicArticlePage t={t} />} />
        <Route
          path="/login"
          element={isAuthenticated ? <Navigate to="/dashboard" replace /> : <LoginPage t={t} onLogin={login} />}
        />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute isAuthenticated={isAuthenticated}>
              <DashboardPage t={t} token={token} />
            </ProtectedRoute>
          }
        />
        <Route path="/moderator" element={<Navigate to="/login" replace />} />
      </Routes>
    </Layout>
  );
}

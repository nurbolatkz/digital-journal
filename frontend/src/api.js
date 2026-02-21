const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api";

const jsonHeaders = {
  "Content-Type": "application/json"
};

async function readErrorMessage(response, fallback) {
  try {
    const data = await response.json();
    if (typeof data?.detail === "string") return data.detail;
    for (const value of Object.values(data || {})) {
      if (Array.isArray(value) && value.length) return String(value[0]);
      if (typeof value === "string") return value;
    }
  } catch {
    // ignore parse errors
  }
  return fallback;
}

export async function fetchPublicArticles({ search = "", category = "", faculty = "" } = {}) {
  const query = new URLSearchParams();
  if (search) query.set("search", search);
  if (category) query.set("category", category);
  if (faculty) query.set("faculty", faculty);

  const response = await fetch(`${API_BASE_URL}/articles/?${query.toString()}`);
  if (!response.ok) throw new Error("Failed to load articles");
  return response.json();
}

export async function fetchPublicArticle(slug) {
  const response = await fetch(`${API_BASE_URL}/articles/${slug}/`);
  if (!response.ok) throw new Error("Failed to load article");
  return response.json();
}

export async function fetchFilterOptions() {
  const response = await fetch(`${API_BASE_URL}/articles/filters/`);
  if (!response.ok) throw new Error("Failed to load filters");
  return response.json();
}

export async function moderatorLogin(username, password) {
  const response = await fetch(`${API_BASE_URL}/auth/token/`, {
    method: "POST",
    headers: jsonHeaders,
    body: JSON.stringify({ username, password })
  });
  if (!response.ok) throw new Error("Invalid credentials");
  return response.json();
}

export async function fetchModeratorArticles(token) {
  const response = await fetch(`${API_BASE_URL}/moderator/articles/`, {
    headers: { Authorization: `Token ${token}` }
  });
  if (!response.ok) throw new Error("Failed to load moderator articles");
  return response.json();
}

export async function fetchModeratorOptions(token) {
  const response = await fetch(`${API_BASE_URL}/moderator/options/`, {
    headers: { Authorization: `Token ${token}` }
  });
  if (!response.ok) throw new Error("Failed to load options");
  return response.json();
}

export async function createArticle(token, payload) {
  const body = new FormData();
  Object.entries(payload).forEach(([key, value]) => {
    if (value === null || value === undefined) return;
    if (key === "pdf_file" && !value) return;
    body.append(key, value);
  });

  const response = await fetch(`${API_BASE_URL}/moderator/articles/`, {
    method: "POST",
    headers: { Authorization: `Token ${token}` },
    body
  });
  if (!response.ok) throw new Error(await readErrorMessage(response, "Failed to create article"));
  return response.json();
}

export async function changeArticleStatus(token, articleId, statusValue) {
  const response = await fetch(`${API_BASE_URL}/moderator/articles/${articleId}/status/`, {
    method: "POST",
    headers: { ...jsonHeaders, Authorization: `Token ${token}` },
    body: JSON.stringify({ status: statusValue })
  });
  if (!response.ok) throw new Error("Failed to update status");
  return response.json();
}

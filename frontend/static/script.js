// ============================================================
// Config — change this to your deployed backend URL
// ============================================================
const API_BASE = window.API_BASE || 'http://localhost:8000';

// ============================================================
// Component loader — injects shared navbar/footer HTML
// ============================================================
async function loadComponent(mountId, path) {
  try {
    const res = await fetch(path);
    const html = await res.text();
    const el = document.getElementById(mountId);
    if (el) el.innerHTML = html;
  } catch (e) {
    console.warn(`Could not load component: ${path}`, e);
  }
}

// ============================================================
// Auth helpers
// ============================================================

function getToken() {
  return localStorage.getItem('token');
}

function logout() {
  localStorage.removeItem('token');
  window.location.href = 'login.html';
}

function requireAuth() {
  if (!getToken()) {
    window.location.href = 'login.html';
  }
}

// ============================================================
// API wrapper
// ============================================================

async function apiFetch(path, options = {}) {
  const token = getToken();
  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...(options.headers || {}),
  };

  const res = await fetch(`${API_BASE}${path}`, { ...options, headers });

  if (res.status === 401) { logout(); return []; }

  const data = await res.json();
  if (!res.ok) {
    throw new Error(data.detail || 'Something went wrong');
  }
  return data;
}
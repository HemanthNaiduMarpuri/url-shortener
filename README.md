# 🔗 URL Shortener – Django

A modern, secure, and scalable **URL Shortener** built with **Django**, featuring authentication, expiry logic, analytics, Redis-based rate limiting (optional), and a polished Tailwind UI with dark mode.

---

## 🚀 Features

### 🔐 Authentication
- User signup & login
- Guest users supported via session tokens
- Secure access to user-specific URLs

### ✂️ URL Shortening
- Base62 encoding using database ID
- Guaranteed uniqueness
- Clean, short URLs

### ⏳ Expiry Logic
- **Guest URLs** expire in **7 days**
- **Authenticated user URLs** expire in **30 days**
- Expired links are automatically invalidated

### 📊 Analytics
- Click count tracking
- URL creation timestamp
- Expiry timestamp

### 📋 Dashboard
- List all user URLs
- Truncated long URLs in list view
- Full URL details on detail page
- Copy-to-clipboard support

### 🎨 UI / UX
- Tailwind CSS
- Dark mode (persistent using localStorage)
- Mobile-first responsive design
- Clean SaaS-style layout

### ⚡ Performance (Optional)
- Redis caching for redirects
- Redis-based rate limiting (graceful fallback if Redis is down)

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django |
| Frontend | Django Templates + Tailwind CSS |
| Database | SQLite (dev) / PostgreSQL (prod-ready) |
| Cache | Redis (optional) |
| Auth | Django Auth |
| Styling | Tailwind CDN |
| JS | Vanilla JavaScript |

---


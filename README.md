# 📝 NoteFlow — A Django Notes App

A full-stack note-taking web application built with Django. Supports user authentication, complete CRUD operations, note categorization, pinning, archiving, and password reset via email.

> Built as a learning project while exploring Django's MVT architecture, ORM, and built-in auth system.

---

## 🚀 Features

- **User Authentication** — Register, Login, Logout with session management
- **Password Reset** — Full email-based reset flow (4-step: request → email → confirm → done)
- **Create / Read / Update / Delete Notes** — Full CRUD with Django forms & ModelForm
- **Categories** — Personal, Work, Study, Health, Finance, Other
- **Tags** — Important, Urgent, Idea, Todo, Reminder, Reference
- **Pin Notes** — Pinned notes appear at the top of the list
- **Archive Notes** — Separate archive section; restore anytime
- **User Isolation** — Every user sees only their own notes
- **Flash Messages** — Success/error feedback on every action

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.11, Django 5.2 |
| Database | SQLite3 (dev) |
| Frontend | Django Templates, Bootstrap 5 |
| Auth | Django's built-in `auth` system |
| Email | Gmail SMTP via `django.core.mail` |
| Config | `python-dotenv` for environment variables |

---

## 📁 Project Structure

```
My Note by Django/
├── core/                   # Project config (settings, root URLs)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/               # Auth app (register, login, logout, password reset)
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/accounts/
│       ├── index.html
│       ├── home.html
│       ├── login.html
│       ├── register.html
│       ├── password_reset.html
│       ├── password_reset_done.html
│       ├── password_reset_confirm.html
│       └── password_reset_complete.html
├── notes/                  # Notes app (CRUD, archive, pin)
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/notes/
│       ├── note_list.html
│       ├── note_detail.html
│       ├── note_form.html
│       ├── note_confirm_delete.html
│       └── note_archive_list.html
├── manage.py
├── requirements.txt        # Project dependencies
├── db.sqlite3
├── .env                    # Not committed — see setup below
└── .gitignore
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/my-note-django.git
cd my-note-django
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> The `requirements.txt` includes only the packages this project actually needs:
> ```
> Django==5.2.17
> python-dotenv==1.2.2
> ```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
EMAIL_USER=your_gmail@gmail.com
EMAIL_PASS=your_gmail_app_password
```

> **Note:** Use a [Gmail App Password](https://myaccount.google.com/apppasswords), not your regular Gmail password. 2-Step Verification must be enabled on your account.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. (Optional) Create a superuser for admin panel

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/accounts/` in your browser.

---

## 🔗 URL Structure

| URL | Description |
|-----|-------------|
| `/accounts/` | Landing page |
| `/accounts/register/` | User registration |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/accounts/home/` | Dashboard (login required) |
| `/accounts/password_reset/` | Request password reset email |
| `/notes/list/` | All active notes |
| `/notes/create/` | Create a new note |
| `/notes/<pk>/` | Note detail view |
| `/notes/<pk>/edit/` | Edit a note |
| `/notes/<pk>/delete/` | Delete a note |
| `/notes/archive/<pk>/` | Archive a note |
| `/notes/archived-notes/` | View archived notes |
| `/notes/unarchive/<pk>/` | Restore from archive |
| `/admin/` | Django admin panel |

---

## 📌 Note Model

```python
class Note(models.Model):
    user       = ForeignKey(User)       # Linked to the logged-in user
    title      = CharField             # Max 255 characters
    content    = TextField             # Optional body
    category   = CharField(choices)    # Personal / Work / Study / Health / Finance / Other
    tag        = CharField(choices)    # Important / Urgent / Idea / Todo / Reminder / Reference
    is_pinned  = BooleanField          # Pinned notes appear first
    is_archived = BooleanField         # Archived notes hidden from main list
    created_at = DateTimeField         # Auto-set on creation
    updated_at = DateTimeField         # Auto-updated on save
```

---

## 🔐 Security Practices

- All note views protected with `@login_required`
- Every query filters by `user=request.user` — no cross-user data access
- CSRF protection enabled globally via Django middleware
- Credentials stored in `.env`, never hardcoded
- `.env` and `db.sqlite3` excluded via `.gitignore`

---

## 🧠 What I Learned

- Django's MVT architecture and request/response lifecycle
- Django ORM — model creation, queries, ForeignKey relationships
- Django's built-in authentication system (`login`, `logout`, `UserCreationForm`)
- Class-based views for password reset (Django's built-in `PasswordResetView` flow)
- ModelForms and form validation
- Flash messages with `django.contrib.messages`
- Organizing a Django project into multiple apps
- Environment variable management with `python-dotenv`

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built by [Dipak](https://github.com/your-username) — learning Django one project at a time.*

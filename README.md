
# 📝 Django Todo List App

A simple Django-based Todo List application with user authentication (login/signup), task management, and deployment support for Render.

## 🔗 Live Demo
[https://django-todolist-w2st.onrender.com](https://django-todolist-w2st.onrender.com)

---

## 🚀 Features

- User registration and login
- Add / edit / delete todo items
- Update task status (Pending, In Progress, Done)
- Due date and timestamp support
- Pagination
- Deployed on Render

---

## 📦 Tech Stack

- Python 3
- Django 5.1.8
- HTML + Bootstrap 5
- SQLite (default)
- Gunicorn + WhiteNoise (for deployment)

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/PhumrapeeC/Django-Todolist.git
cd Django-Todolist
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser 🎉

---

## 🌐 Deployment (Render)

1. Set environment variables on Render:
   - `SECRET_KEY` — your Django secret key
   - `DEBUG` — `False`
   - `ALLOWED_HOSTS` — `your-app-name.onrender.com,localhost`

2. Add this to your `requirements.txt`:

```
gunicorn
whitenoise
dj-database-url
```

3. Add to `render.yaml`:

```yaml
services:
  - type: web
    name: django-todo-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn mysite.wsgi:application
```

4. Run this before pushing to production:

```bash
python manage.py collectstatic
```

---

## 📂 Project Structure

```
mysite/
├── settings.py
├── urls.py
├── wsgi.py
todoapp/
├── templates/
├── static/
├── views.py
├── models.py
├── forms.py
├── urls.py
```

---

## 🙌 Author

- [Phumrapee Chaowanapricha](https://github.com/PhumrapeeC)

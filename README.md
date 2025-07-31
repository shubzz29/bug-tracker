# 🐞 Bug Tracker – Django Web App

A minimal and functional bug tracking system built with Django. This project allows users to report, view, and track bugs in a software development environment.

---

## 🚀 Features

- ✅ Submit new bug reports with title, description, priority, and status
- 📋 View all reported bugs in a tabular list
- 🔎 Click on individual bugs to view detailed information
- 📅 Auto-generated timestamps for bug creation and updates
- 🔒 Admin interface for managing bug reports
- 🧱 Built with Django (MVC framework)

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Django 4.x**
- HTML/CSS for frontend
- SQLite3 (default DB)

---
1. **Clone the repository**

 git clone https://github.com/shubzz29/bug-tracker.git
 cd bug-tracker

1. **Create virtual environment

 python3 -m venv venv
 source venv/bin/activate  # For Linux/macOS
 venv\Scripts\activate     # For Windows

3. **Install dependencies

 pip install -r requirements.txt

4. **Run migrations

   python manage.py makemigrations
   python manage.py migrate

5. **Run development server

   python manage.py runserver

🧪 Testing (Optional)
You can create a superuser to access the admin panel:

python manage.py createsuperuser


Then go to http://127.0.0.1:8000/admin/ and log in.

📄 License
This project is open source and available under the MIT License.

👨‍💻 Author
Made with ❤️ by Shubham Pawar


 

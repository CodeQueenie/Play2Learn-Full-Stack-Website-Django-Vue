**Project Setup**
This Full-Stack web application is built with Django and Vue, utilizing Bootstrap for primary layout and styling, and Font Awesome for icons.

To properly test and interact with this website, follow these setup steps:

1. Create a virtual environment by running:
```
python -m venv .venv
```
2. Activate the virtual environment:
- For Windows: `.venv/Scripts/activate`
- For Mac/Linux: `source .venv/bin/activate`

3. Install required packages:
```
pip install -r requirements.txt
```

**Database Setup**
This project uses PostgreSQL as the backend database. To set it up:
1. Update the database configuration in `play2learn/settings.py`.
2. Create the necessary database in PostgreSQL (using pgAdmin or terminal).

If you prefer using SQLite:
Update the database details as follows:
```
"ENGINE": "django.db.backends.sqlite3",
"NAME": BASE_DIR / "db.sqlite3",
```

Migrate the database by running:
```
python manage.py migrate
```

**SendGrid Email Setup**
For automated emails using SendGrid, you will need a SendGrid account, make the following updates:
1. Update `DEFAULT_FROM_EMAIL` in `play2learn/settings.py`.
2. Update `SENDGRID_API_KEY` in `play2learn/local_settings.py`.

**Compiling and Running for Development**
Ensure the virtual environment is active, then run:
1. For backend server:
```
python manage.py runserver
```
2. For frontend Vue app:
```
npm install
npm run serve
npm run build
```

This will launch both backend and frontend local servers. Enjoy testing the website!

For comprehensive Django setup instructions and project details, refer to the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).

**DjangoPlay2Learn Overview**
This project showcases skills in HTML, CSS, JavaScript, Python, Django, Vue, and Bootstrap. Utilized SQLite database for simplicity and maintained in development/debug mode.

For any queries or assistance, feel free to reach out. Happy coding! 🚀

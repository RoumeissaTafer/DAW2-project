\# DAW2 Project – Full Stack Platform

Technologies: \*\*Django (Backend) + PostgreSQL (Database) + React (Frontend)\*\*



This repository contains the full-stack project for the DAW2 module.  

The project is organized into two main parts: \*\*backend\*\* and \*\*frontend\*\*.



---



\## 📁 Project Structure



```

DAW2-project/

&nbsp;  backend/        → Django backend (API + business logic)

&nbsp;  frontend/       → React frontend (UI)

&nbsp;  README.md

&nbsp;  .gitignore

```



---



\## 🔧 Backend (Django)



\### 📌 Requirements

Only \*\*backend developers + database developer\*\* need to install:



\- Python 3.10+

\- Django

\- PostgreSQL (only DB girl needs it)



\### 📌 Install backend dependencies



Move into backend folder:



```

cd backend

pip install -r requirements.txt

```



\### 📌 Run backend server



```

python manage.py runserver

```



Backend will run on:

```

http://127.0.0.1:8000/

```



---



\## 🗄️ Database (PostgreSQL)



Only the database girl needs PostgreSQL installed.



\### She must provide:

\- `DB\_NAME`

\- `DB\_USER`

\- `DB\_PASSWORD`

\- `DB\_HOST`

\- `DB\_PORT`



These values must be added in backend → `event\_platform/settings.py` in the DATABASES section.



All migrations will be shared through GitHub.



---



\## 🎨 Frontend (React)



Only frontend developers need:



\- Node.js

\- npm



\### Install dependencies



Move to frontend folder:



```

cd frontend

npm install

```



\### Run React server



```

npm start

```



Frontend runs on:

```

http://localhost:3000/

```



---



\## 🌳 Branching Strategy



Each team member works in their own branch:



```

git checkout -b chaimab

git checkout -b frontend-maram

git checkout -b hiba

git checkout -b database-ikram

```



---



\## 🤝 Contributors



\- Meissa (Backend Leader)

\- Hiba (Backend)

\- Ikram (Database)

\- Chaima (Frontend)

\- Maram (Frontend)



---






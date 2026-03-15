# 🔐 Secure Notepad

Secure Notepad is a web-based note management application built using **Python Flask**.  
It allows users to securely create, store, edit, and delete personal notes through a simple and clean web interface.

The application focuses on **user authentication and secure data handling**, ensuring that each user can only access their own notes.

---

## 🚀 Features

- User Registration and Login System
- Secure Password Hashing
- Create, Read, Update, and Delete Notes (CRUD)
- Session-based Authentication
- User-specific Note Storage
- Simple and Responsive UI
- SQLite Database Integration

---

## 🛠 Technologies Used

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**
- **HTML**
- **CSS**
- **Werkzeug (Password Hashing)**

---

## 📂 Project Structure

```
Secure-Notepad
│
├── app/
│   ├── auth/
│   ├── notes/
│   ├── models.py
│   └── __init__.py
│
├── templates/
│
├── static/
│
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/Secure-Notepad.git
```

2. Navigate to the project directory

```bash
cd Secure-Notepad
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python run.py
```

5. Open your browser and go to

```
http://127.0.0.1:5000/
```

---

## 🔒 Security Features

- Passwords are stored using **secure hashing**
- Each user can only access **their own notes**
- Authentication required for accessing note features
- Session-based login protection

---

## 🎯 Project Objective

The objective of this project is to demonstrate how a secure web application can be built using the **Flask framework**, including authentication, database management, and secure data handling.

---

## 👨‍💻 Author

**Kashish Mukharjee**
Lovely Professional University
B.Tech CSE

---

## 📌 Future Improvements

- End-to-end encryption for notes
- Cloud deployment
- Two-factor authentication
- Rich text editor for notes

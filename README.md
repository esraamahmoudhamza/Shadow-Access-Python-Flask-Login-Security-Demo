# ShadowAccess - Flask Authentication Security Demo

ShadowAccess is a backend-focused authentication demo built with Python and Flask.  
The project simulates a login system to demonstrate how authentication works on the server side and how access control logic protects restricted pages.

This project is designed for educational purposes in cybersecurity and backend development.

---

## 🎯 Project Purpose

This project helps developers understand:

- How login requests are handled by a backend server
- How credentials are validated securely on the server side
- How protected routes work
- What happens when authentication succeeds or fails
- The difference between frontend validation and backend validation

It is ideal for beginners learning cybersecurity concepts or backend development with Flask.

---

## 🔐 Features

- Server-side credential validation  
- Protected dashboard route  
- Access granted / access denied responses  
- Clean authentication flow  
- Structured Flask routing  
- Simple responsive UI  
- Beginner-friendly project structure  

---

## 🛠 Technologies Used

- Python 3.x  
- Flask  
- HTML5  
- CSS3  

---

## 📂 Project Structure

```
shadowaccess/
│
├── app.py
├── templates/
│   ├── login.html
└── static/
    └── style.css
```

---

## ⚙️ How It Works

1. User submits username and password.
2. The server receives the POST request.
3. Flask validates the credentials.
4. If correct → user is redirected to a protected dashboard.
5. If incorrect → access is denied.

This demonstrates the basic authentication flow used in real-world applications.

---

## 🚨 Security Awareness

This demo is intentionally simplified for learning purposes.

It does NOT include:

- Password hashing (e.g., Argon2, bcrypt)
- Database integration
- Session management hardening
- CSRF protection
- Rate limiting
- Brute-force protection

In production environments, these security layers are mandatory.

---

## 🚀 Future Improvements

- Add password hashing (Argon2 / bcrypt)
- Implement login attempt limiting
- Add session-based authentication
- Connect to a secure database
- Add JWT authentication version

---

## 📄 License

This project is open source and available under the MIT License.

---

## 📌 Author

Esraa Codes  
© 2026

---

## 🔗 Follow Me

Stay connected for more cool projects & tutorials 🚀

- 📸 [Instagram](https://www.instagram.com/esraa_codes)
- 🎵 [TikTok](https://www.tiktok.com/@esraa.codes)
- ▶️ [YouTube](https://www.youtube.com/@EsraaCodes)
- 🌐 [GitHub](https://github.com/esraamahmoudhamza)

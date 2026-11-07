# 🔐 Secure Login System

A beginner-friendly, terminal-based authentication system developed using Python. This project demonstrates fundamental cybersecurity concepts such as password hashing, salting, password verification, account lockout, and secure data storage.

## 📌 Project Overview

The Secure Login System allows users to register and log in using a username and password. Instead of storing passwords in plain text, the application uses **PBKDF2-HMAC-SHA256** with randomly generated salts to securely derive password hashes.

User information and account lockout status are stored persistently in a JSON file.

## ✨ Features

- **User Registration:** Create an account using a unique username and password.
- **Password Hashing:** Uses PBKDF2-HMAC-SHA256 to derive password hashes.
- **Random Salt Generation:** Generates a unique 16-byte cryptographically secure salt for each password.
- **Password Verification:** Verifies login credentials using the stored salt and password hash.
- **Secure Comparison:** Uses `hmac.compare_digest()` for comparing password hashes.
- **Password Masking:** Uses Python's `getpass` module to hide password input in the terminal.
- **Account Lockout:** Locks an account after three consecutive incorrect password attempts.
- **Persistent Storage:** Stores user credentials and locked account information in JSON format.
- **Input Error Handling:** Handles invalid menu input without terminating the application.
- **Modular Programming:** Separates authentication, password hashing, and file handling into different Python modules.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| hashlib | PBKDF2-HMAC-SHA256 password hashing |
| secrets | Cryptographically secure random salt generation |
| hmac | Secure hash comparison |
| getpass | Hidden password input |
| json | Persistent data storage |

**External dependencies:** None. The project uses Python's standard library.

## 📂 Project Structure

```text
Secure-Login-System/
│
├── secure_login.py       # Main application and authentication logic
├── password_hashing.py   # Password hashing and verification
├── file_handling.py      # JSON file storage and retrieval
├── users.json            # Local user data (generated at runtime)
├── .gitignore            # Excludes sensitive and unnecessary files
└── README.md             # Project documentation
```

## 🔑 How Password Hashing Works

This project uses PBKDF2-HMAC-SHA256 to protect stored passwords.

### Registration Process

1. User enters a password.
2. A random 16-byte salt is generated using `secrets.token_bytes()`.
3. PBKDF2-HMAC-SHA256 derives a password hash using 600,000 iterations.
4. The salt and derived hash are converted into hexadecimal strings.
5. The salt and hash are stored in `users.json`, not the original password.

### Login Verification Process

1. User enters their username and password.
2. The application retrieves the stored salt and password hash.
3. The entered password is processed using PBKDF2 with the original salt.
4. The newly derived hash is compared with the stored hash using `hmac.compare_digest()`.
5. If the hashes match, access is granted; otherwise, the login attempt is rejected.

## ⚙️ Installation and Execution

### Prerequisites

- Python 3 installed on your system.
- Git (optional, for cloning the repository).

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Secure-Login-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Secure-Login-System
```

### 3. Run the Application

```bash
python secure_login.py
```

The application will display a menu:

```text
===================
SECURE LOGIN SYSTEM
===================

1. Register
2. Login
3. Exit
```

Follow the terminal instructions to register an account or log in.

## 🧪 Security Concepts Demonstrated

- Password hashing versus plain-text password storage.
- Random salts and why they are necessary.
- Key derivation using PBKDF2.
- Secure password verification.
- Limiting authentication attempts.
- Basic account lockout mechanisms.
- Persistent storage of authentication data.

## ⚠️ Limitations and Disclaimer

This project is developed for **educational purposes and cybersecurity learning**. It is not intended for production use.

Some limitations include:

- Account lockout currently has no automatic recovery or administrator unlock mechanism.
- JSON storage does not provide database-level security or protection against file tampering.
- Additional input validation and corrupted-file handling are needed.
- No multi-factor authentication or password reset functionality is implemented.

For real-world authentication systems, additional security controls and established authentication frameworks should be used.

## 🎯 Learning Objectives

The primary goal of this project is to strengthen Python programming fundamentals while understanding how authentication systems protect user credentials.

It also provides practical experience with Python modules, functions, dictionaries, sets, exception handling, cryptographic libraries, and file handling.

---

**Author:** Your Name

**Project:** Secure Login System

**Domain:** Python Programming | Cybersecurity | Authentication Security
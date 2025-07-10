
import tkinter as tk
from tkinter import messagebox
import sqlite3

Initialize database
def init_db():
    conn = sqlite3.connect("studyhub.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
     Default user
    c.execute("INSERT OR IGNORE INTO users (email, password) VALUES (?, ?)", ("admin@study.com", "1234"))
    conn.commit()
    conn.close()

Validate login
def validate_login(email, password):
    conn = sqlite3.connect("studyhub.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    result = c.fetchone()
    conn.close()
    return result is not None

 Action on login
def login():
    email = email_entry.get()
    password = password_entry.get()
    if validate_login(email, password):
        messagebox.showinfo("Success", f"Welcome, {email}!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

 Create login window
init_db()
window = tk.Tk()
window.title("Login - Study Hub")
window.geometry("400x600")
window.configure(bg="#1a1a2e")

tk.Label(window, text="Login", font=("Arial", 30, "bold"), fg="white", bg="#1a1a2e").pack(pady=40)
tk.Label(window, text="Sign in to continue.", font=("Arial", 12), fg="white", bg="#1a1a2e").pack()

 Email field
tk.Label(window, text="EMAIL", fg="white", bg="#1a1a2e", anchor="w").pack(pady=(30, 5))
email_entry = tk.Entry(window, font=("Arial", 14), width=30)
email_entry.pack()
Password field
tk.Label(window, text="PASSWORD", fg="white", bg="#1a1a2e", anchor="w").pack(pady=(20, 5))
password_entry = tk.Entry(window, font=("Arial", 14), show="*", width=30)
password_entry.pack()

Login Button
tk.Button(window, text="Login", font=("Arial", 14), width=20, command=login).pack(pady=30)

window.mainloop()
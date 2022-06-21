from re import L
import sqlite3

def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username text, password text, email text, role text)")
    conn.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS times (id INTEGER PRIMARY KEY AUTOINCREMENT, time text)")
    conn.commit()
    conn.close()

def insert(username,password,email,role):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (NULL,?,?,?,?)",(username,password,email,role))
    conn.commit()
    conn.close()

def check_user_psw(username, password):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    if cur.fetchone() is not None:
        return True
    else:
        return False

def get_times():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM times")
    times = cur.fetchall()
    conn.close()

    return times

def get_users():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    conn.close()

    return users

def update_role(id, role):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE users SET role=? WHERE id=?",(role,id))
    conn.commit()
    conn.close()

def delete_user(id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE from users WHERE id=?",(id))
    conn.commit()
    conn.close()

def update_time(id, new_time):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE times SET time=? WHERE id=?",(new_time,id))
    conn.commit()
    conn.close()
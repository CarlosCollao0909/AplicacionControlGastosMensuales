import sqlite3


def create_db():
    conn = sqlite3.connect('gastos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(nombre, apellido, email, password):
    conn = sqlite3.connect('gastos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nombre, apellido, email, password)
        VALUES (?, ?, ?, ?)
    ''', (nombre, apellido, email, password))
    conn.commit()
    conn.close()

def verify_user(email, password):
    conn = sqlite3.connect('gastos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None
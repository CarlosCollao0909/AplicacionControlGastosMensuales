import sqlite3
from datetime import datetime

def create_db():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    
    # Crear la tabla de usuarios
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )''')
    
    # Crear la tabla de saldo
    c.execute('''CREATE TABLE IF NOT EXISTS saldo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER NOT NULL,
                    saldo_individual REAL NOT NULL,
                    saldo_total REAL NOT NULL,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                )''')
    
    # Crear la tabla de gastos
    c.execute('''CREATE TABLE IF NOT EXISTS gastos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER NOT NULL,
                    descripcion TEXT NOT NULL,
                    monto REAL NOT NULL,
                    fecha DATE NOT NULL,
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                )''')
    
    conn.commit()
    conn.close()

def add_user(nombre, apellido, email, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO usuarios (nombre, apellido, email, password) VALUES (?, ?, ?, ?)", 
                (nombre, apellido, email, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(email, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE email = ? AND password = ?", (email, password))
    user = c.fetchone()
    conn.close()
    return user is not None

def get_user_data(email):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("SELECT nombre, apellido, email FROM usuarios WHERE email = ?", (email,))
        user = c.fetchone()
        return user
    except sqlite3.Error as e:
        print(f"Error al obtener datos del usuario: {e}")
        return None
    finally:
        conn.close()

def get_user_id(email):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
        user_id = c.fetchone()
        return user_id[0] if user_id else None
    except sqlite3.Error as e:
        print(f"Error al obtener ID del usuario: {e}")
        return None
    finally:
        conn.close()

def add_saldo(usuario_id, nuevo_monto):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    
    try:
        conn.execute('BEGIN')
        
        saldo_actual = get_saldo(usuario_id)
        saldo_total = saldo_actual + nuevo_monto
        
        c.execute("""
            INSERT INTO saldo (usuario_id, saldo_individual, saldo_total) 
            VALUES (?, ?, ?)
        """, (usuario_id, nuevo_monto, saldo_total))
        
        conn.commit()
        return True
        
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error al añadir saldo: {e}")
        return False
        
    finally:
        conn.close()

def get_saldo(usuario_id):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    
    try:
        c.execute("""
            SELECT saldo_total 
            FROM saldo 
            WHERE usuario_id = ? 
            ORDER BY fecha DESC LIMIT 1
        """, (usuario_id,))
        saldo = c.fetchone()
        return saldo[0] if saldo else 0.0
        
    except sqlite3.Error as e:
        print(f"Error al obtener saldo: {e}")
        return 0.0
        
    finally:
        conn.close()

def get_historial_saldos(usuario_id):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("""
            SELECT saldo_individual, saldo_total, fecha 
            FROM saldo 
            WHERE usuario_id = ? 
            ORDER BY fecha DESC
        """, (usuario_id,))
        historial = c.fetchall()
        return historial
    except sqlite3.Error as e:
        print(f"Error al obtener historial de saldos: {e}")
        return []
    finally:
        conn.close()

def buscar_saldos_por_fecha(usuario_id, fecha_inicio, fecha_fin):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("""
            SELECT saldo_individual, saldo_total, fecha 
            FROM saldo 
            WHERE usuario_id = ? AND fecha BETWEEN ? AND ?
            ORDER BY fecha DESC
        """, (usuario_id, fecha_inicio, fecha_fin))
        saldos = c.fetchall()
        return saldos
    except sqlite3.Error as e:
        print(f"Error al buscar saldos por fecha: {e}")
        return []
    finally:
        conn.close()

def get_total_saldo_periodo(usuario_id, fecha_inicio, fecha_fin):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("""
            SELECT SUM(saldo_individual) 
            FROM saldo 
            WHERE usuario_id = ? AND fecha BETWEEN ? AND ?
        """, (usuario_id, fecha_inicio, fecha_fin))
        total = c.fetchone()[0]
        return total if total else 0.0
    except sqlite3.Error as e:
        print(f"Error al obtener total del periodo: {e}")
        return 0.0
    finally:
        conn.close()

def registrar_gasto(usuario_id, descripcion, monto, fecha):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    
    try:
        conn.execute('BEGIN')
        
        saldo_actual = get_saldo(usuario_id)
        
        if saldo_actual < monto:
            return False, "Saldo insuficiente para realizar el gasto"
        
        nuevo_saldo_total = saldo_actual - monto
        
        # Registrar el gasto
        c.execute("""
            INSERT INTO gastos (usuario_id, descripcion, monto, fecha) 
            VALUES (?, ?, ?, ?)
        """, (usuario_id, descripcion, monto, fecha))
        
        # Registrar la reducción en el saldo
        c.execute("""
            INSERT INTO saldo (usuario_id, saldo_individual, saldo_total) 
            VALUES (?, ?, ?)
        """, (usuario_id, -monto, nuevo_saldo_total))
        
        conn.commit()
        return True, "Gasto registrado exitosamente"
        
    except sqlite3.Error as e:
        conn.rollback()
        return False, f"Error en la base de datos: {str(e)}"
        
    finally:
        conn.close()

def get_gastos_usuario(usuario_id):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("""
            SELECT id, descripcion, monto, fecha, fecha_registro
            FROM gastos 
            WHERE usuario_id = ?
            ORDER BY fecha_registro DESC
        """, (usuario_id,))
        gastos = c.fetchall()
        return gastos
    except sqlite3.Error as e:
        print(f"Error al obtener gastos del usuario: {e}")
        return []
    finally:
        conn.close()

def delete_gasto(gasto_id, usuario_id):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    
    try:
        conn.execute('BEGIN')
        
        # Obtener el monto del gasto antes de eliminarlo
        c.execute("SELECT monto FROM gastos WHERE id = ? AND usuario_id = ?", 
                 (gasto_id, usuario_id))
        gasto = c.fetchone()
        
        if not gasto:
            return False, "Gasto no encontrado"
            
        monto_gasto = gasto[0]
        
        # Eliminar el gasto
        c.execute("DELETE FROM gastos WHERE id = ? AND usuario_id = ?", 
                 (gasto_id, usuario_id))
        
        # Obtener el saldo actual
        saldo_actual = get_saldo(usuario_id)
        
        # Calcular el nuevo saldo total (devolviendo el monto del gasto)
        nuevo_saldo_total = saldo_actual + monto_gasto
        
        # Registrar la devolución en el saldo
        c.execute("""
            INSERT INTO saldo (usuario_id, saldo_individual, saldo_total) 
            VALUES (?, ?, ?)
        """, (usuario_id, monto_gasto, nuevo_saldo_total))
        
        conn.commit()
        return True, "Gasto eliminado exitosamente"
        
    except sqlite3.Error as e:
        conn.rollback()
        return False, f"Error en la base de datos: {str(e)}"
        
    finally:
        conn.close()

def get_gastos_por_fecha(usuario_id, fecha_inicio, fecha_fin):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("""
            SELECT id, descripcion, monto, fecha, fecha_registro
            FROM gastos 
            WHERE usuario_id = ? AND fecha BETWEEN ? AND ?
            ORDER BY fecha_registro DESC
        """, (usuario_id, fecha_inicio, fecha_fin))
        gastos = c.fetchall()
        return gastos
    except sqlite3.Error as e:
        print(f"Error al obtener gastos por fecha: {e}")
        return []
    finally:
        conn.close()

def get_total_gastos_periodo(usuario_id, fecha_inicio, fecha_fin):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("""
            SELECT SUM(monto) 
            FROM gastos 
            WHERE usuario_id = ? AND fecha BETWEEN ? AND ?
        """, (usuario_id, fecha_inicio, fecha_fin))
        total = c.fetchone()[0]
        return total if total else 0.0
    except sqlite3.Error as e:
        print(f"Error al obtener total de gastos del periodo: {e}")
        return 0.0
    finally:
        conn.close()
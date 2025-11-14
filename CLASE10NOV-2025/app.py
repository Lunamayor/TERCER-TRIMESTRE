from flask import Flask, request, jsonify, render_template  # CORRECCIÓN IMPORTS
import psycopg2  # Conexión a PostgreSQL
from psycopg2.extras import RealDictCursor  # Obtener datos como diccionario
from datetime import datetime  # CORRECCIÓN IMPORT datetime
import os  # Variables del sistema

# Configuración de la aplicación Flask
app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'database': 'datos',
    'user': 'postgres',
    'password': '123456',
    'port': '5432',
}

def conectar_db():
    try:
        conexion = psycopg2.connect(**DB_CONFIG)
        return conexion
    except psycopg2.Error:
        return None

# Crear tabla Usuario
def crear_tabla_usuario():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuario (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conexion.commit()
        cursor.close()
        conexion.close()

# Ruta principal
@app.route('/')
def inicio():
    return render_template('index.html')  # CORREGIDO

# Ruta para guardar usuarios
@app.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():
    try:
        conexion = conectar_db()
        if conexion is None:
            return jsonify({'mensaje': 'Error de conexión'}), 500

        datos = request.get_json()
        nombre = datos.get('nombre')   # CORREGIDO
        email = datos.get('email')     # CORREGIDO
        fecha_creacion = datetime.now()

        if not nombre or not email:
            return jsonify({'mensaje': 'El nombre y el correo son obligatorios'}), 400

        cursor = conexion.cursor()
        sql_insert = """
        INSERT INTO Usuario (nombre, email)
        VALUES (%s, %s, %s)
        RETURNING id;
        """

        cursor.execute(sql_insert, (nombre, email))
        usuario_id = cursor.fetchone()[0]

        conexion.commit()
        cursor.close()
        conexion.close()

        return jsonify({'mensaje': 'Usuario guardado exitosamente', 'usuario_id': usuario_id})

    except Exception as e:
        return jsonify({'mensaje': 'Error al guardar el usuario', 'error': str(e)}), 500

# Obtener usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    try:
        conexion = conectar_db()
        if conexion is None:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500

        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM Usuario ORDER BY id DESC;")  # CORREGIDO

        usuarios = cursor.fetchall()
        
        cursor.close()
        conexion.close()

        # Formatear fecha
        for u in usuarios:
            if u['fecha_creacion']:
                u['fecha_creacion'] = u['fecha_creacion'].strftime('%Y-%m-%d %H:%M:%S')

        return jsonify(usuarios), 200

    except Exception as e:
        return jsonify({'mensaje': 'Error al obtener los usuarios', 'error': str(e)}), 500


if __name__ == "__main__":
    crear_tabla_usuario()
    app.run(debug=True)

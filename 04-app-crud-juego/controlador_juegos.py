# Importacion de la funcion de conección
from bd import obtener_conexion

# Controlador: obtener_juegos
def obtener_juegos():
    conexion = obtener_conexion()
    juegos = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos")
        juegos = cursor.fetchall()
    conexion.close()
    return juegos

# Controlador: insertar_juego
def insertar_juego(nombre, descripcion, precio):
    # Establesco conexion
    conexion = obtener_conexion()
    # Almaceno en base de datos las tres variables que vienen desde el formulario y son recibidas por la vista
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO juegos (nombre, descripcion, precio) VALUES (%s,%s,%s)",(nombre, descripcion, precio))
    conexion.commit()
    conexion.close()


def eliminar_juego(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM juegos WHERE id = %s",(id,))
    conexion.commit()
    conexion.close

def obtener_juego(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM juegos WHERE id = %s",(id,))
    conexion.commit()
    conexion.close()

# Controlador: obtener_juego_id
def obtener_juego_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, descripcion, precio FROM juegos WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego

# Controlador: actualizar_juego
def actualizar_juego(nombre, descripcion, precio, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE juegos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",(nombre, descripcion, precio, id))
    conexion.commit()
    conexion.close()

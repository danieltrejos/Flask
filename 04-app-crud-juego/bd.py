# Conexion a la base de datos
# Se importa el conector de la base de datos %pip install pymysql
import pymysql

# Configuracion de los datos de la conexion
def obtener_conexion():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="daniel",
        db="app_crud_juego"
)
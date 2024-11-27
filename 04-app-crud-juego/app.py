"""CRUD FLASK PYTHON + MYSQL"""
# Import necessary modules from Flask 

from flask import Flask, render_template,request,redirect,flash

# Importacion completa controlador de juegos y todas las funciones
import controlador_juegos

# Instancia de flask

app = Flask(__name__)

# Ruta principal
@app.route("/")
@app.route("/juegos")
def juegos():
    juegos = controlador_juegos.obtener_juegos()
    return render_template("juegos.html", juegos=juegos)

# Ruta agregar juego
@app.route("/agregar_juego")
def formulario_agregar_juego():
    return render_template("agregar_juego.html")

# Ruta guardar juego -> Funcion del controlador en la ruta 

@app.route("/guardar_juego", methods=["POST"])
def guardar_juego():
    
    # Obtener datos del formulario
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    
    # Guarda los datos en la base de datos ingresando a la funcion insertar juego del controlador
    controlador_juegos.insertar_juego(nombre, descripcion, precio)
    
    # Mostrar mensaje de exito
    #flash("Juego agregado exitosamente!")
    
    # Redireccionar a la lista de juegos
    return redirect("/juegos")

# Ruta eliminar Juego
@app.route("/eliminar_juego", methods=["POST"])
def eliminar_juego():
    controlador_juegos.eliminar_juego(request.form["id"])
    return redirect("/juegos")


# Ruta formulario editar juego
@app.route("/editar_juego/<int:id>")
def editar_juego(id):
    # Obtener al juego por ID
    juego = controlador_juegos.obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)

# Ruta: actualizar_juego
@app.route("/actualizar_juego", methods=["POST"])
def actualizar_juego():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_juegos.actualizar_juego(nombre, descripcion, precio, id)
    return redirect("/juegos")



# Iniciar el servididor para ejecutar flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000, debug=True)

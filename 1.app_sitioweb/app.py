from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

# nosotros,servicios,contactos

@app.route("/nosotros")
def nosostros():
    return render_template('nosotros.html')

@app.route("/servicios")
def servicios():
    return render_template('servicios.html')

@app.route("/contacto")
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug = True)

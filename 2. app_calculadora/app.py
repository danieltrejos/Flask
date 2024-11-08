from flask import Flask, request, render_template,redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

# Ruta principal que muestra el formulario y calculadora aritmetica
@app.route("/", methods=["GET", "POST"])
def aritmetica():
    if request.method == "POST":
        # Valores que recibo del formulario
        num1 = float(request.form.get("n1"))
        num2 = float(request.form.get("n2"))

        # Operaciones
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2

        # Retornar variables
        return render_template("index.html", total_suma=suma,
                                            total_resta=resta, 
                                            total_multiplicacion=multiplicacion, 
                                            total_division=division)

        pass
    return render_template("index.html")

# Ruta para divisas
@app.route("/divisas", methods=["GET", "POST"])
def divisas():
    if request.method == "POST":
        # Valores que recibo del formulario
        usd = float(request.form.get("usd"))

        # Operaciones
        cop = usd * 4305
        eur = usd * 0.93    
        mxn = round(usd * 23.38,1)

        # Retornar variables
        return render_template("divisas.html", cop=cop,
                                            eur=eur, 
                                            mxn=mxn,
                                            dolar=usd)

        pass
    return render_template("divisas.html")

# Ejecuto el servidor

if __name__ == "__main__":
    app.run(debug=True)
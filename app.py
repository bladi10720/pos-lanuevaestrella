from flask import Flask, render_template, request
import sqlite3
import datetime

app = Flask(__name__)

def obtener_productos():
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, nombre, precio FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

@app.route("/", methods=["GET", "POST"])
def index():
    carrito = []
    total = 0
    if request.method == "POST":
        codigos = request.form.getlist("codigo")
        conn = sqlite3.connect("productos.db")
        cursor = conn.cursor()
        for codigo in codigos:
            cursor.execute("SELECT nombre, precio FROM productos WHERE codigo = ?", (codigo,))
            producto = cursor.fetchone()
            if producto:
                carrito.append(producto)
                total += producto[1]
        conn.close()
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return render_template("ticket.html", carrito=carrito, total=total, fecha=fecha)
    productos = obtener_productos()
    return render_template("index.html", productos=productos)

if __name__ == "__main__":
    app.run(debug=True)

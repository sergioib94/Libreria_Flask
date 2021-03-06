from flask import Flask, render_template, abort
import os
import json
app = Flask(__name__)

with open("books.json") as fichero:
    datos=json.load(fichero)

@app.route('/')
def inicio():
	return render_template("inicio.html",libros=datos)

@app.route('/libro/<isbn>')
def libro(isbn):
    for detalles in datos:
        if "isbn" in detalles.keys() and isbn == detalles["isbn"]:
            return render_template("libro.html",libro=detalles)
    abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
    for cat in datos:
        if "categories" in cat.keys() and categoria in cat["categories"]:
            return render_template("categorias.html",libros=datos, categoria=categoria)
    abort(404)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=False)

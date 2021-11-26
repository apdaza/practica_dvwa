from flask import Flask, render_template, request, redirect, url_for
from pymongo.message import delete
from models.modelo import *
from models.cifrado import *

app = Flask(__name__)

@app.route('/')
def listar():
    edit = cifrar("editar")
    delete = cifrar("eliminar")
    data = consultar()
    return render_template('listar.html', data=data, edit=edit, delete=delete)

@app.route('/<accion>/<id>')
def renviar(accion, id):
    accion = descifrar(accion[2:-1])
    if accion == "editar":
        return redirect(url_for('editar', id=id))
    elif accion == "eliminar":
        return redirect(url_for('eliminar', id=id))

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'GET':
        return render_template('agregar.html')
    else:
        info = request.form
        data = {
            'nombre': info['nombre'],
            'apellido': info['apellido'],
            'edad': info['edad']
        }
        insertar(data)
        return redirect(url_for('listar'))

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'GET':
        data = consultar(id)
        print(data)
        return render_template('editar.html', data=data)
    else:
        info = request.form
        data = {
            'nombre': info['nombre'],
            'apellido': info['apellido'],
            'edad': info['edad']
        }
        actualizar(id, data)
        return redirect(url_for('listar'))

@app.route('/eliminar/<id>')
def eliminar(id):
    borrar(id)
    return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(debug=True)
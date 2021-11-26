from flask import Flask, render_template, request, redirect, url_for
from models.modelo import *

app = Flask(__name__)

@app.route('/')
def listar():
    data = consultar()
    return render_template('listar.html', data=data)

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
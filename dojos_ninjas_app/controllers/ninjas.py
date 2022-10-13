from dojos_ninjas_app import app
from dojos_ninjas_app.models.ninja import Ninja
from dojos_ninjas_app.models.dojo import Dojo
from flask import render_template, redirect, request


@app.route("/ninjas")
def formulario_ninja():
    todos_dojos = Dojo.todos_dojos()
    return render_template('ninjas.html', todos_dojos=todos_dojos)


@app.route("/crearninja", methods=['POST'])
def crearninja():
    #id_ninja = Ninja.crearninja(request.form)
    
    data = {
        'first_name':request.form['nombre'],
        'last_name':request.form['apellido'],
        'edad':request.form['edad'],
        'dojo_id':request.form['dojo'],
    }
    id_ninja = Ninja.crearninja(data)
    #un_ninja=Ninja.obtener_un_ninja(data)
    return redirect(f'/dojos/{data["dojo_id"]}')


@app.route('/ninjas/<int:ninjas_id>')
def show_ninjas(ninjas_id):
    data = {"id":ninjas_id}
    ninja = Ninja.obtener_un_ninja(data)
    ninjas_de_un_dojo = Dojo.obtener_ninjas_del_dojo(data)
    return render_template('show.html', ninja=ninja, ninjas_de_un_dojo=ninjas_de_un_dojo)
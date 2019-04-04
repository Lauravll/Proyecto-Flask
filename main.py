#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import redirect
from flask import Flask, url_for
import dbpython
from flask import jsonify
from clases.Usuario import Usuario, Sesion

import forms

app = Flask(__name__, template_folder = "vistas")
app.secret_key = 'my_secret_key'
csrf = CSRFProtect()
csrf.init_app(app)

#http://127.0.0.1:8000/client
@app.route('/docente', methods= ['GET', 'POST'])
def index():
	nombre_cookie = request.cookies.get('nombre_cookie', 'indefinido') #cookie
	print nombre_cookie
	titulo = 'Sistema'
	titulo = titulo.decode('utf-8')
	return render_template('index.html', titulo=titulo)
	
@app.route('/creartp', methods= ['GET', 'POST'])
def creartp():
	titulo = 'Sistema'
	titulo = titulo.decode('utf-8')
	creartp_form = forms.CrearTPForm(request.form)#crea instancia con datos enviados
	if request.method == 'POST' and creartp_form.validate():
		nombre = creartp_form.titulo.data
		print(nombre)
		carrera = creartp_form.carrera.data
		print(carrera)
		materia = request.form.get('materia')
		print(materia)
		user =Usuario(None,None,None,None,None)
		sesion=Sesion()
		usuario2=sesion.traerUsuarioComprobado('sss')
		try:
			print("Usuario: "+ usuario2.getNombre())
			numero = usuario2.crearTrabajoPractico(nombre, materia, carrera)
			print("TP " + numero +" creado con éxito")
		except Exception:
			print("Error al insertar TP")
		'''

		print("Error al insertar TP")
	args = {'nombreP': nombreP, , 'nombre': nombre, 'materia': materia, 'carrera': carrera, 'usuario1': usuario}'''
		return redirect(url_for('hacertp', titulotp= nombre, idtrabajo= numero))
		
		#return render_template('htrabajo.html', titulo=titulo, form = creartp_form, materia=request.form.get('materia'))
	else:
		print "Error en el formulario"
	return render_template('creartp.html', titulo=titulo, form = creartp_form)

@app.route('/hacertp/<titulotp>/<idtrabajo>', methods= ['GET', 'POST'])
def hacertp(titulotp, idtrabajo):
	
	return render_template('htrabajo.html', nombre=titulotp, idtrabajo = idtrabajo)	
	
@app.route('/materia/<carrera>')
def materia(carrera):
	print (carrera)
	form = forms.CrearTPForm(request.form)#crea instancia con datos enviados
	cursor = dbpython.db.cursor()
	sql = "SELECT * FROM materia where idCarrera = '" + str(carrera) + "'"
	cursor.execute(sql)
	lista = cursor.fetchall()
	cities2 = []
	for row in lista:
		materiaObj2 = {}
		materiaObj2['id'] = str(row[0])
		materiaObj2['name'] = row[1]
		cities2.append(materiaObj2)
		#print row[1]
	print cities2

	return jsonify({'cities' : cities2})

@app.route('/', methods= ['GET', 'POST'])
def login():
	titulo = 'Sistema'
	titulo = titulo.decode('utf-8')
	login_form = forms.LoginForm(request.form)#crea instancia con datos enviados
	if request.method == 'POST' and login_form.validate():
		print (login_form.username2.data)
		print (login_form.clave.data)
		return redirect(url_for('index'))
	else:
		print "Error en el formulario"
	return render_template('login.html', titulo=titulo, form = login_form)

@app.route('/cookie')
def cookiefunc():
    response = make_response( render_template("cookies.html"))
    response.set_cookie('nombre_cookie', 'Locky')
    return response


if __name__ == '__main__':
	app.run(debug = True, port= 8000)

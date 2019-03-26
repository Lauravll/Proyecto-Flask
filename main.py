#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response

import forms

app = Flask(__name__, template_folder = "vistas")
app.secret_key = 'my_secret_key'
csrf = CSRFProtect()
csrf.init_app(app)

#http://127.0.0.1:8000/client
@app.route('/', methods= ['GET', 'POST'])
def index():
	nombre_cookie = request.cookies.get('nombre_cookie', 'indefinido') #cookie
	print nombre_cookie
	titulo = 'Proyecto'
	titulo = titulo.decode('utf-8')
	comment_form = forms.CommentForm(request.form)#crea instancia con datos enviados
	if request.method == 'POST' and comment_form.validate():
		print (comment_form.username.data)
		print (comment_form.email.data)
		print (comment_form.comment.data)
	else:
		print "Error en el formulario"
	return render_template('index.html', titulo=titulo, form = comment_form)

@app.route('/cookie')
def cookiefunc():
    response = make_response( render_template("cookies.html"))
    response.set_cookie('nombre_cookie', 'Locky')
    return response

if __name__ == '__main__':
	app.run(debug = True, port= 8000)

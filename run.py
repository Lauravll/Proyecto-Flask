#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder = "vistas")

#http://127.0.0.1:8000/client
@app.route('/docente')
def client():
	lista_nombre = ['Test1', 'Test2', 'Test3', 'Test4']
	return render_template('index.html', list=lista_nombre)
	
if __name__ == '__main__': 
	app.run(debug = True, port= 8000)

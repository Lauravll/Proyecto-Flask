#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms import Form
from wtforms import StringField, TextField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from  wtforms import validators
import dbpython
from clases.Carrera import Carrera
from clases.Materia import Materia
from flask_wtf import FlaskForm 

def campo_vacio(form, field):
	if len(field.data) > 0:
		raise validators.ValidationError('El campo debe estar vacio.')

class CrearTPForm(FlaskForm):
	titulo = StringField('Titulo:',[
	validators.Required()
	])
	cursor = dbpython.db.cursor()
	sql = "SELECT * FROM carrera"
	cursor.execute(sql)
	lista = cursor.fetchall()
	ch = []
	for row in lista:
		ch.append((str(row[0]), row[1]))
		print str(row[0])
	ch.append((0, ''))
	carrera = SelectField('Carrera:', choices=ch, default=0) 
	
	
class LoginForm(Form):
	username2 = StringField('Usuario:',[
	validators.Required()
	])
	clave = StringField('Clave:',[
	validators.Required()
	])
	vacio = HiddenField('', [campo_vacio])

	

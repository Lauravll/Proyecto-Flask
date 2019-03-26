#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from  wtforms import validators

def campo_vacio(form, field):
	if len(field.data) > 0:
		raise validators.ValidationError('El campo debe estar vacio.')

class CommentForm(Form):
	username = StringField('Usuario:',[
	validators.Required()
	])
	email = EmailField('Correo electronico:',[
	validators.Required()
	])
	comment = TextField('Comentario: ')
	vacio = HiddenField('', [campo_vacio])

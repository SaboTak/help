from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators ,SubmitField, ValidationError, TextField
from wtforms import validators, HiddenField
from wtforms.validators import InputRequired,EqualTo



def length_honypot(form,field):
    if len(field.data)>0:
        raise validators.ValidationError('El campo debe estar vacio.')

class LoginForm(Form):
    username = StringField('Usuario',
            [
            validators.Required(message ='El Usuario es requerido.'),
            validators.length(min=0, max=15, message='Ingrese un Usuario Valido.')
            ])
    password = PasswordField('Contraseña', [validators.Required(message='La contraseña es requerida.')])
    submit = SubmitField('Entrar')
    honypot = HiddenField('',[length_honypot])

class ChangeForm(Form):
    password = PasswordField('Contraseña Actual',
                            [InputRequired(),validators.length(min=3,max=30, message='La contraseña debe tener minimo 3 caracteres.')]
                            )
    new_password = PasswordField('Nueva Contraseña',
                                [InputRequired(), EqualTo('confirm_password', message='Las contraseñas no coinciden.') , validators.length(min=6,max=30, message='La contraseña debe tener minimo 6 caracteres.')]
                                )
    confirm_password = PasswordField('Confirmar Contraseña')
    submit = SubmitField('actualizar')
    honypot = HiddenField('',[length_honypot])
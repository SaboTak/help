import os


from flask import Flask, session, render_template, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import request, make_response
from werkzeug import secure_filename
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators ,SubmitField
from wtforms import validators
from flask import url_for,json, g
from flask_wtf.csrf import CSRFProtect
from flask import flash
import forms
import flask
import sys
from config import BaseConfig


app = Flask(__name__, static_folder=os.path.abspath('static'))
app.config.from_object(BaseConfig)



# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



# extras


 # Routes
@app.route("/")
def render():
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route("/index")
def index():
    user = 'Login'
    #print (g.test) #cerrar = g.test.close
    if 'username' in session:
        user = session["nick"]
    return render_template('index.html',user=user)


@app.route("/news")
def news():
    user = "Login"
    if 'username' in session:
        user = session["nick"]
    return render_template('news.html',user=user)


@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route("/nosotros")
def nosotros():
    user = "Login"
    if 'username' in session:
        user = session["nick"]
    return render_template('nosotros.html',user=user)

@app.route("/creditos")
def creditos():
    user = "Login"
    if 'username' in session:
        user = session["nick"]
    return render_template('creditos.html',user=user)


@app.route("/servicio")
def servicio():
    user = "Login"
    if 'username' in session:
        user = session["nick"]
    return render_template('servicio.html',user=user)

@app.route("/servicios")
def servicios():
    user = "Login"
    if 'username' in session:
        user = session["nick"]
    return render_template('servicios.html',user=user)

@app.route("/documentos")
def documentos():
    user = "Login"
    if 'username' in session:
        user = session["nick"]
    return render_template('documentos.html',user=user)


@app.route("/unete")
def unete():
    user = "Login"
    if 'username' in session:
        user = session["nick"]
    return render_template('unete.html',user=user)




@app.route("/login", methods= ['GET','POST'])
def login():
    user= "Login"
    login_form = forms.LoginForm(request.form)
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST' and login_form.validate():
            username = login_form.username.data
            password = login_form.password.data
            data = db.execute("SELECT * FROM users WHERE cedula = :a", {"a":username}).fetchone()
            if data != None:
                if data.cedula == username and data.password == password:
                    person = db.execute("SELECT cedula FROM asociados WHERE cedula = :e", {"e":username}).fetchone()
                    user = data.nombre
                    session["nick"] = user
                    session["username"] = username
                    success_message = 'Bienvenido(a) {}'.format(user)
                    flash(success_message)
                    if data.estado == True:
                        return redirect(url_for('change'))
                    else:
                        return redirect(url_for('index'))
                else:
                    error_message = 'Usuario o Contraseña Incorrectos'
                    flash(error_message)
            else:
                error_message = 'Usuario o Contraseña Incorrectos'
                flash(error_message)
    return render_template('login.html',form = login_form,user=user)


@app.route("/changes", methods= ['GET','POST'])
def change():
    user = "Login"
    change_form = forms.ChangeForm(request.form)
    if 'username' in session:
        username = session["username"]
        get = db.execute("SELECT * FROM users WHERE cedula = :e", {"e": username}).fetchone()
        user = get.nombre
        actual = get.password

        if request.method == 'POST' and change_form.validate():
            password = change_form.password.data
            new_password = change_form.new_password.data
            confirm_password = change_form.confirm_password.data
            if password == actual:
                cambio = db.execute("UPDATE users SET password = :new_password WHERE password = :password",{"new_password": confirm_password, "password":actual})
                if cambio is not None:
                    db.commit()
                    estado = db.execute("UPDATE users SET estado = 'f' WHERE password= :password",{"password":new_password})
                    db.commit()
                    success_message = 'Cambio Exitoso.'
                    flash(success_message)
                    return redirect(url_for('index'))
                else:
                    success_message = 'Error Al cambiar .'
                    flash(success_message)

        #success_message = '{} Has cambiado tu contraseña!'.format(user)
        #flash(success_message)

    else:
        return redirect(url_for('login'))


    return render_template('changes.html',form = change_form, user=user)




@app.route('/acount', methods= ['GET','POST'])
def acount():
    user = 'Login'
    if 'username' in session:
        usernam = session["username"]
        data = db.execute("SELECT * FROM asociados WHERE cedula= :username",{"username": usernam}).fetchone()
        cedula = data.cedula
        asociado = data.asociado
        aporte = data.aporte
        prestamo = data.prestamo
        suministro = data.suministro
        db.commit()
        user = session["nick"]

        return render_template('acount.html', user=user , cedula = cedula , asociado = asociado, aporte = aporte, prestamo = prestamo, suministro = suministro)

    else:
        return redirect(url_for('login'))





#@app.route('/ajax-login', methods =['POST'])
#def ajax_login():
#    print (request.form)
#    username = request.form['username']
#    response = {'status':200 , 'username': username, 'id': 1}
#    return json.dumps(response)
if __name__  ==  '__main__':
    app.run(debug=os.getenv('DEBUG'))

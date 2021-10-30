#Mauricio Colque Morales
from re import template
from flask import (
    Flask,
    g, #available thorugh the request context, global to request
    redirect,
    render_template,
    request,
    session,
    url_for
)
from flask_session import Session
from Usuario import *

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        #There should be a user tho
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('pag1'))
            #logs in correctly

        #if the user fails to provide a password
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if validate_on_username(username):
            new_user = User(id, username, password)
            users.append(new_user)

            return redirect(url_for('login'))

    return render_template('register.html', users=users)





@app.route("/pag1")
def pag1():
    #if not g.user:
     #   return redirect(url_for('login'))   
    session["datos_personales"] = []
    return render_template("pag1.html")


@app.route("/pag2", methods=["POST"])
def pag2():

    if len(session["datos_personales"]) == 0:
        datos = ["nombres", "apellidos", "titulo", "direccion", 
                "ciudad", "pais", "telefono",
                "email", "presentacion", "linkedin"]

        for dato in datos:
            session["datos_personales"].append(request.form.get(dato))

        #Para que los primeros datos no sean 'NONE' 

        session["exp_laboral"] = []
        session["estudios"] = []
        session["logros"] = []
        session["habilidades"] = []
        session["referencias"] = []        
        session["intereses"] = None
        return render_template("pag2.html")


    #Estudios
    temporal = [request.form.get("lugar"), request.form.get("estudio"), 
                request.form.get("est_inicio"),  request.form.get("est_fin")]

    if lista_llenada(temporal):
        session["estudios"].append(temporal)

    #Experiencia laboral
    temporal = [request.form.get("accion"), request.form.get("puesto"),
                request.form.get("exp_inicio"), request.form.get("exp_fin")]

    if lista_llenada(temporal):
        session["exp_laboral"].append(temporal)
    
    #Logros
    temporal = request.form.get("logro")
    if variable_llenada(temporal):
        session["logros"].append(temporal)

    return render_template("pag2.html", estudios=session["estudios"], exp_laboral = session["exp_laboral"], logros=session["logros"])



@app.route("/pag3", methods=["POST"])
def pag3():

    if (session["intereses"] == None) or (session["habilidades"] == None) or session["referencias"] == None:
        session["intereses"] = []
        session["habilidades"] = []
        session["referencias"] = []
        session["seleccion"] = None
        return render_template("pag3.html")

    #Habilidades
    temporal = [request.form.get("habilidad"), request.form.get("dominio")]

    if lista_llenada(temporal):
        #Agregar solo en caso haya sido llenada
        session["habilidades"].append(temporal) 

    #Intereses
    temporal = request.form.get("interes")
    if variable_llenada(temporal):
        session["intereses"].append(temporal)
        
    #Referencias
    temporal = [request.form.get("r_email"), request.form.get("r_telefono")]

    if lista_llenada(temporal):
        session["referencias"].append(temporal)

    return render_template("pag3.html", habilidades=session["habilidades"], intereses=session["intereses"], referencias=session["referencias"])


@app.route("/pag4", methods=["POST"])
def pag4():
    if session["seleccion"] == None:
        session["seleccion"] = []
        temporal = request.form.get("opcion")
        session["seleccion"].append(temporal)
        return render_template("pag4.html", seleccion=session["seleccion"])



@app.route("/plantilla", methods=["POST"])
def plantilla_cv():
    return render_template("cv.html", datos_personales=session["datos_personales"], exp_laboral=session["exp_laboral"], 
                            estudios=session["estudios"], logros=session["logros"], habilidades=session["habilidades"], 
                            intereses=session["intereses"], referencias=session["referencias"] )



@app.route("/plantilla2", methods=["POST"])
def plantilla_cv2():
    return render_template("cv2.html",datos_personales=session["datos_personales"], exp_laboral=session["exp_laboral"], 
                            estudios=session["estudios"], logros=session["logros"], habilidades=session["habilidades"], 
                            intereses=session["intereses"], referencias=session["referencias"] )

@app.route("/plantilla3", methods=["POST"])
def plantilla_cv3():
    return render_template("cv3.html",datos_personales=session["datos_personales"], exp_laboral=session["exp_laboral"], 
                            estudios=session["estudios"], logros=session["logros"], habilidades=session["habilidades"], 
                            intereses=session["intereses"], referencias=session["referencias"] )
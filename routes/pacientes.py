from conexion import *
from models.pacientes import mi_pacientes

@programa.route("/pacientes")
def pacientes():
    if session.get("login")==True:
        resultado = mi_pacientes.consultar()
        return render_template("pacientes.html",resul = resultado)
    else:
        return redirect("/")

@programa.route("/agrega_paciente")
def agrega_paciente():
    if session.get("login")==True:
        return render_template("agrega_paciente.html")
    else:
        return redirect("/")

@programa.route("/guarda_paciente", methods=["POST"])
def guarda_paciente():
    id = request.form["id"]
    nom = request.form["nom"]
    mail = request.form["mail"]
    cel = request.form["cel"]
    foto = request.files["foto"]
    resultado = mi_pacientes.buscar(id)
    if len(resultado)==0:
        mi_pacientes.agregar(id,nom,mail,cel,foto)
        return redirect("/pacientes")
    else:
        return render_template("agrega_paciente.html", msg="ID ya está en uso")

@programa.route("/modifica_paciente/<id>")
def modifica_paciente(id):
    if session.get("login")==True:
        pacientes = mi_pacientes.buscar(id)
        return render_template("modifica_paciente.html", paciente=pacientes[0])
    else:
        return redirect("/")

@programa.route("/actualiza_paciente", methods=['POST'])
def actualiza_paciente():
    id = request.form["id"]
    nom = request.form["nom"]
    mail = request.form["mail"]
    cel = request.form["cel"]
    foto = request.files["foto"]
    mi_pacientes.actualizar(id,nom,mail,cel,foto)
    return redirect("/pacientes")

@programa.route("/borra_paciente/<id>")
def borra_paciente(id):
    if session.get("login")==True:
        mi_pacientes.borrar(id)
        return redirect("/pacientes")
    else:
        return redirect("/")

@programa.route("/envia_mail/<id>")
def envia_mail(id):
    if session.get("login")==True:
        mi_pacientes.envia_mail(id)
        return redirect("/pacientes")
    else:
        return redirect("/")
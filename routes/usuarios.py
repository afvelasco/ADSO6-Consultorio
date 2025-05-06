from conexion import *
from models.usuarios import mi_usuarios

@programa.route("/login", methods = ['POST'])
def login():
    id = request.form['id']
    contra = request.form['contra']
    resultado = mi_usuarios.loguear(id,contra)
    if len(resultado)==0:
        return render_template("index.html",msg="Credenciales incorrectas")
    else:
        session["login"] = True
        session["id"] = id
        session["nombre"] = resultado[0][0]
        return redirect("/opciones")


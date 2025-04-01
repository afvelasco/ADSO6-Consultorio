from conexion import *
from models.pacientes import mi_pacientes

@programa.route("/uploads/<nombre>")
def uploads(nombre):
    return send_from_directory(programa.config['CARPETAU'],nombre)

@programa.route("/")
def raiz():
    return render_template("index.html")

@programa.route("/login", methods = ['POST'])
def login():
    id = request.form['id']
    contra = request.form['contra']
    cifrada = hashlib.sha512(contra.encode("utf-8")).hexdigest()
    sql = f"SELECT nombre FROM usuarios WHERE id='{id}' AND contra='{cifrada}'"
    mi_cursor.execute(sql)
    resultado=mi_cursor.fetchall()
    if len(resultado)==0:
        return render_template("index.html",msg="Credenciales incorrectas")
    else:
        session["login"] = True
        session["id"] = id
        session["nombre"] = resultado[0][0]
        return redirect("/opciones")

@programa.route("/opciones")
def opciones():
    if session.get("login")==True:
        nom = session.get("nombre")
        return render_template("opciones.html", nom=nom)
    else:
        return redirect("/")
        
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
    mi_cursor = mi_db.cursor()
    sql = f"SELECT nombre FROM pacientes WHERE id='{id}'"
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    if len(resultado)==0:
        ahora = datetime.now()
        fecha = ahora.strftime("%Y%m%d%H%M%S")
        nombre,extension = os.path.splitext(foto.filename)
        nueva_foto = "U"+fecha+extension
        foto.save("uploads/"+nueva_foto)
        sql = f"INSERT INTO pacientes (id,nombre,email,celular,foto) VALUES ('{id}','{nom}','{mail}','{cel}','{nueva_foto}')"
        mi_cursor.execute(sql)
        mi_db.commit()
        return redirect("/pacientes")
    else:
        return render_template("agrega_paciente.html", msg="ID ya está en uso")

@programa.route("/modifica_paciente/<id>")
def modifica_paciente(id):
    if session.get("login")==True:
        mi_cursor = mi_db.cursor()
        sql = f"SELECT * FROM pacientes WHERE id='{id}'"
        mi_cursor.execute(sql)
        pacientes = mi_cursor.fetchall()
        return render_template("modifica_paciente.html", paciente=pacientes[0])
    else:
        return redirect("/")

@programa.route("/actualiza_paciente", methods=['POST'])
def actualiza_paciente():
    id = request.form["id"]
    nom = request.form["nom"]
    mail = request.form["mail"]
    cel = request.form["cel"]
    mi_cursor = mi_db.cursor()
    sql = f"UPDATE pacientes SET nombre='{nom}', email='{mail}', celular='{cel}' WHERE id='{id}'"
    mi_cursor.execute(sql)
    mi_db.commit()
    return redirect("/pacientes")

@programa.route("/borra_paciente/<id>")
def borra_paciente(id):
    if session.get("login")==True:
        mi_cursor = mi_db.cursor()
        sql = f"UPDATE pacientes SET borrado=1 WHERE id='{id}'"
        mi_cursor.execute(sql)
        mi_db.commit()
        return redirect("/pacientes")
    else:
        return redirect("/")

if __name__=="__main__":
    programa.run(debug=True, host="0.0.0.0", port=5080)



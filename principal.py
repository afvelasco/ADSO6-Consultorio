from conexion import *
import routes.pacientes

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
        
if __name__=="__main__":
    programa.run(debug=True, port=5080)



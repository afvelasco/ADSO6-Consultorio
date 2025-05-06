from conexion import *
import routes.pacientes
import routes.usuarios

@programa.route("/uploads/<nombre>")
def uploads(nombre):
    return send_from_directory(programa.config['CARPETAU'],nombre)

@programa.route("/")
def raiz():
    return render_template("index.html")

@programa.route("/opciones")
def opciones():
    if session.get("login")==True:
        nom = session.get("nombre")
        return render_template("opciones.html", nom=nom)
    else:
        return redirect("/")
        
if __name__=="__main__":
    programa.run(debug=True, port=5080)



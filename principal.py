from flask import Flask, redirect, render_template, request
import mysql.connector

programa = Flask(__name__)
mi_db = mysql.connector.connect(host="localhost",
                                port="3306",
                                user="root",
                                password="",
                                database="consultorio06")

@programa.route("/pacientes")
def pacientes():
    mi_cursor = mi_db.cursor()
    sql = "SELECT * FROM pacientes WHERE borrado=0"
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    return render_template("pacientes.html",resul = resultado)

@programa.route("/agrega_paciente")
def agrega_paciente():
    return render_template("agrega_paciente.html")

@programa.route("/guarda_paciente", methods=["POST"])
def guarda_paciente():
    id = request.form["id"]
    nom = request.form["nom"]
    mail = request.form["mail"]
    cel = request.form["cel"]
    mi_cursor = mi_db.cursor()
    sql = f"SELECT nombre FROM pacientes WHERE id='{id}'"
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    if len(resultado)==0:
        sql = f"INSERT INTO pacientes (id,nombre,email,celular) VALUES ('{id}','{nom}','{mail}','{cel}')"
        mi_cursor.execute(sql)
        mi_db.commit()
        return redirect("/pacientes")
    else:
        return render_template("agrega_paciente.html", msg="ID ya está en uso")

@programa.route("/modifica_paciente/<id>")
def modifica_paciente(id):
    mi_cursor = mi_db.cursor()
    sql = f"SELECT * FROM pacientes WHERE id='{id}'"
    mi_cursor.execute(sql)
    pacientes = mi_cursor.fetchall()
    return render_template("modifica_paciente.html", paciente=pacientes[0])

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


if __name__=="__main__":
    programa.run(debug=True, host="0.0.0.0", port=5080)



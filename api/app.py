from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import mysql.connector

app = Flask(__name__)
api = Api(app)
mi_DB = mysql.connector.connect(host="localhost",
                                port=3306,
                                user="root",
                                password="",
                                database="consultorio06")
mi_cursor = mi_DB.cursor()

class EspecialistaLista(Resource):
    def get(self):
        sql = f"SELECT * FROM especialistas"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        especialistas = []
        for esp in resultado:
            especialistas.append({"id" :esp[0],"nombre":esp[1],"especialidad":esp[2],"foto":esp[3]})
        return jsonify({"especialistas": especialistas})
    
    def post(self):
        nuevo_esp = request.json
        sql = f"SELECT * FROM especialistas WHERE id_especialista='{nuevo_esp["id"]}'"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        if len(resultado)==0:
            sql = f"INSERT INTO especialistas (id_especialista,nombre,especialidad,foto) VALUES ('{nuevo_esp["id"]}','{nuevo_esp["nombre"]}','{nuevo_esp["especialidad"]}','{nuevo_esp["foto"]}')"
            mi_cursor.execute(sql)
            mi_DB.commit()
            return jsonify({"mensaje" : "Especialista Agregado"})
        else:
            return jsonify({"mensaje" : "Id de Especialista ya existe"})

class Especialista(Resource):
    def get(self, id):
        sql = f"SELECT * FROM especialistas WHERE id_especialista='{id}'"
        mi_cursor.execute(sql)
        esp = mi_cursor.fetchall()
        if len(esp)>0:
            esp = esp[0]
            return jsonify({"id":esp[0], "nombre":esp[1], "especialidad":esp[2], "foto": esp[3]})
        else:
            return jsonify({"mensaje":"Especialista no encontrado"})
        
    def put(self, id):
        esp = request.json
        sql = f"SELECT * FROM especialistas WHERE id_especialista='{id}'"
        mi_cursor.execute(sql)
        esp = mi_cursor.fetchall()
        if len(esp)>0:
            sql = f"UPDATE especialistas SET nombre='{esp[1]}', especialidad='{esp[2]}', foto='{esp[3]}' WHERE id_especialista='{esp[0]}'"
            return jsonify({"mensaje":"Especalista actualizado"})
        else:
            return jsonify({"mensaje":"Especialista no encontrado"})
    
    def delete(self, id):
        sql = f"SELECT * FROM especialistas WHERE id_especialista='{id}'"
        mi_cursor.execute(sql)
        esp = mi_cursor.fetchall()
        if len(esp)>0:
            sql = f"DELETE FROM especialistas WHERE id_especialista='{id}'"
            return jsonify({"mensaje":"Especalista eliminado"})
        else:
            return jsonify({"mensaje":"Especialista no encontrado"})

        
api.add_resource(EspecialistaLista,"/especialistas")
api.add_resource(Especialista,"/especialistas/<int:id>")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8001)
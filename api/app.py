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
        print(nuevo_esp)
        sql = f"INSERT INTO especialistas (id_especialista,nombre,especialidad,foto) VALUES ('{nuevo_esp["id"]}','{nuevo_esp["nombre"]}','{nuevo_esp["especialidad"]}','{nuevo_esp["foto"]}')"
        mi_cursor.execute(sql)
        mi_DB.commit()
        return jsonify({"mensaje" : "Especialista Agregado"})
"""
class ProductoItem(Resource):
    def get(self,id):
        for item in productos:
            if item['id']==id:
                return jsonify(item)
        return jsonify({"mensaje":"Producto no encontrado"})
    """
        
api.add_resource(EspecialistaLista,"/especialistas")
#api.add_resource(ProductoItem,"/productos/<int:id>")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8001)
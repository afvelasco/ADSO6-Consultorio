import requests

id = input("Id: ")
nombre = input("Nombre: ")
especialidad = input("Especialidad: ")

nuevo_esp = {"id":id, "nombre":nombre, "especialidad": especialidad, "foto": ""}
respuesta = requests.post("http://10.6.125.199:8001/especialistas", json = nuevo_esp)
print(respuesta)
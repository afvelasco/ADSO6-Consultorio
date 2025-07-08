import requests

id = input("Id: ")
nombre = input("Nombre: ")
especialidad = input("Especialidad: ")
opcion = input("(A)gregar/(M)odificar/(B)orrar/(L)istado/(U)no: ")
nuevo_esp = {"id":id, "nombre":nombre, "especialidad": especialidad, "foto": ""}
if opcion =="A":
    respuesta = requests.post(f"http://10.6.126.39:8001/especialistas", json = nuevo_esp)
elif opcion == "M":
    respuesta = requests.put(f"http://10.6.126.39:8001/especialistas/{id}", json = nuevo_esp)
elif opcion == "B":
    respuesta = requests.delete(f"http://10.6.126.39:8001/especialistas/{id}")
elif opcion == "L":
    respuesta = requests.get(f"http://10.6.126.39:8001/especialistas")
elif opcion == "U":
    respuesta = requests.get(f"http://10.6.126.39:8001/especialistas/{id}")
else:
    respuesta = {"mensaje":"Opción no disponible"}
print(respuesta.json())
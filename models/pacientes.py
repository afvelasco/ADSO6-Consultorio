from conexion import *

class Pacientes:
    def consultar(self):
        sql = "SELECT * FROM pacientes WHERE borrado=0"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        return resultado

mi_pacientes = Pacientes()

from conexion import *

class Usuario:
    def loguear(self, id, contra):
        cifrada = hashlib.sha512(contra.encode("utf-8")).hexdigest()
        sql = f"SELECT nombre FROM usuarios WHERE id='{id}' AND contra='{cifrada}'"
        print(sql)
        mi_cursor.execute(sql)
        resultado=mi_cursor.fetchall()
        return resultado

mi_usuarios = Usuario()
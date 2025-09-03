from conexion import *
from models.usuarios import mi_usuarios
import hashlib
import pytest

class Test_usuario:
    def setup_class(self):
        # Se prepara el entorno de prueba
        cifrada = hashlib.sha512("florecita".encode("UTF-8")).hexdigest()
        sql = f"INSERT INTO usuarios (id,contra) VALUES ('antonia','{cifrada}')"
        mi_cursor.execute(sql)
        mi_db.commit()

    @pytest.mark.parametrize(
        ["id_entrada","contra_entrada","esperado"],
        [("antonia","florecita",1),
        ("antonia","floresita",0),
        ("pepe","djlfsk",0)]
    )
    
    def test_valida_login(self,id_entrada,contra_entrada,esperado):
        # Se ejecuta la prueba
        resultado = mi_usuarios.loguear(id_entrada,contra_entrada)
        # Se verifica el resultado
        assert len(resultado) == esperado
        
    def teardown_class(self):
        # Se limpia la base de datos
        sql=f"DELETE FROM usuarios WHERE id='antonia'"
        mi_cursor.execute(sql)
        mi_db.commit()
        

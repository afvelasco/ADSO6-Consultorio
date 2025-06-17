from conexion import *

class Pacientes:
    def consultar(self):
        sql = "SELECT * FROM pacientes WHERE borrado=0"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        return resultado
    
    def buscar(self, id):
        sql = f"SELECT * FROM pacientes WHERE id='{id}'"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        return resultado

    def agregar(self,id,nom,mail,cel,foto):
        ahora = datetime.now()
        fecha = ahora.strftime("%Y%m%d%H%M%S")
        nombre,extension = os.path.splitext(foto.filename)
        nueva_foto = "U"+fecha+extension
        foto.save("uploads/"+nueva_foto)
        sql = f"INSERT INTO pacientes (id,nombre,email,celular,foto) VALUES ('{id}','{nom}','{mail}','{cel}','{nueva_foto}')"
        mi_cursor.execute(sql)
        mi_db.commit()

    def actualizar(self,id,nom,mail,cel,foto):
        if foto.filename!="":
            resultado = mi_pacientes.buscar(id)
            nombre_foto = resultado[0][4]
            os.remove(os.path.join(programa.config['CARPETAU'],nombre_foto))
            ahora = datetime.now()
            fecha = ahora.strftime("%Y%m%d%H%M%S")
            nombre,extension = os.path.splitext(foto.filename)
            nueva_foto = "U"+fecha+extension
            foto.save("uploads/"+nueva_foto)
        sql = f"UPDATE pacientes SET nombre='{nom}', email='{mail}', celular='{cel}', foto='{nueva_foto}' WHERE id='{id}'"
        mi_cursor.execute(sql)
        mi_db.commit()
    
    def borrar(self,id):
        sql = f"UPDATE pacientes SET borrado=1 WHERE id='{id}'"
        mi_cursor.execute(sql)
        mi_db.commit()
        
    def envia_mail(self, id):
        paciente = mi_pacientes.buscar(id)
        nombre = paciente[0][1]
        destinatario = paciente[0][2]
        remitente = "adso06-cab@outlook.com"
        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = "Prueba desde Python"
        cuerpo = "Este es un mensaje de prueba enviado desde Aplicación (Python)"
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        password = "kuuvgjumsgzjaivs"
        server = smtplib.SMTP('smtp.office365.com:587')
        server.starttls()
        server.login(remitente, password)
        server.sendmail(remitente, destinatario, mensaje.as_string())
        server.quit()
        print("¡Mensaje enviado!")

mi_pacientes = Pacientes()

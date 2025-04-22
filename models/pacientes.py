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
        mensaje['To'] = ', '.join(destinatario)
        mensaje['Subject'] = "Prueba de email desde python"
        cuerpo = f"Hola {nombre}, este es un mensaje de prueba desde python"
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        usuario = 'adso06-cab@outlook.com'
        password = 'C4b-S3n4-4ds0oG'
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp_server:
            smtp_server.ehlo()  # Puede omitirse
            smtp_server.starttls()  # Asegura la conexión
            smtp_server.ehlo()  # Puede omitirse
            smtp_server.login(usuario, password)
            smtp_server.sendmail(remitente, destinatario, mensaje.as_string())
#        server = smtplib.SMTP('smtp-mail.outlook.com',587)
#        server.ehlo()
#        server.starttls()
#        server.ehlo
#        server.login(usuario,password)
#        server.sendmail(remitente,destinatario,mensaje.as_string())
#        server.quit()
        return True

mi_pacientes = Pacientes()

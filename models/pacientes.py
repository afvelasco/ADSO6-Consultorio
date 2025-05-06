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
        asunto = "Prueba desde Python"
        cuerpo = f"Mensaje para {nombre}, enviado como una prueba desde python"
        remitente = "adso06-cab@outlook.com"
        password = "C4b-S3n4-4ds0oG"
        msg = MIMEMultipart()
        msg['Subject'] = asunto
        msg['From'] = remitente
        msg['To'] = ', '.join(destinatario)
        msg.attach(MIMEText(cuerpo, 'plain'))
        servidor = smtplib.SMTP('live.smtp.mailtrap.io', 587)
        servidor.ehlo()
        servidor.starttls()
        servidor.ehlo()
        servidor.login(remitente, password)
        servidor.send_message(msg)
        servidor.quit()
        print("¡Mensaje enviado!")
        return True

mi_pacientes = Pacientes()

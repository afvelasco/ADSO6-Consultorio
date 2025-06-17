from datetime import datetime, timedelta
import hashlib
import os
from random import randint
from flask import Flask, redirect, render_template, request, send_from_directory, session
import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

programa = Flask(__name__)
mi_db = mysql.connector.connect(host="localhost",
                                port="3306",
                                user="root",
                                password="",
                                database="consultorio06")
mi_cursor = mi_db.cursor()
programa.config['CARPETAU'] = os.path.join('uploads')
programa.secret_key = "LaMasSegura"
programa.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

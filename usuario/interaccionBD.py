#interaccionBD.py
import psycopg2
from Usuario import *

def conectarse():
    conexion = psycopg2.connect(
        database = "chat_escritorio",
        host = "localhost",
        user = "postgres",
        password = "12345",
        port = "5432"
    )
    cursor = conexion.cursor()
    return cursor, conexion
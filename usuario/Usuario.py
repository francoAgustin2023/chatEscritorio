#Usuario.py
from interaccionBD import conectarse

class Usuario:

    lista = []

    @classmethod
    def recuperarUsuarios(cls): #DEBE EJECUTARSE SIEMPRE EN 1ER LUGAR PARA QUE LA LISTA ESTE LLENA
        cursor, conexion = conectarse()
        cursor.execute("SELECT * FROM usuario;")
        resultado = cursor.fetchall()
        for tupla in resultado:
            usuario = cls(*tupla)
            Usuario.lista.append(usuario)
        conexion.commit()
        cursor.close()
        conexion.close()

    @classmethod 
    def guardarNuevoUsuario(cls, nuevoUsuario):
        cursor, conexion = conectarse()
        for usuario in cls.lista:
            if nuevoUsuario.nombre == usuario.nombre or nuevoUsuario.correo == usuario.correo:
                print(f"/// NO SE CREO EL USUARIO {nuevoUsuario.nombre} POR YA EXISTIR ///")
                return False # no se creara el nuevo usuario por ya existir

        #si no existe no hay problemas 
        datos = (nuevoUsuario.nombre, nuevoUsuario.apodo, nuevoUsuario.correo, nuevoUsuario.contrasenia)
        #id no se carga porque en postgres hay un serial que lo hace automatico y respeta el orden
        consultaInsert = "INSERT INTO usuario (nombre, apodo, correo, contrasenia) VALUES (%s, %s, %s, %s)"
        cursor.execute (consultaInsert, datos)
        conexion.commit()
        cursor.close()
        conexion.close()
        #refrescamos la lista
        cls.recuperarUsuarios()
        print(f"/// NUEVO USUARIO {nuevoUsuario.nombre} AGREGADO CORRECTAMENTE! ///")

    def __init__(self, id, nombre, apodo, correo, contrasenia):
        self.id = id
        self.nombre = nombre
        self.apodo = apodo
        self.correo = correo
        self.contrasenia = contrasenia

    def __str__(self):
        return f"usuario con id: {self.id}\n\tNombre: {self.nombre}\n\tApodo: {self.apodo}\n\tCorreo: {self.correo}"
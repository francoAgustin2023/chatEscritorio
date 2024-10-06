#run.py
from Usuario import *
from interaccionBD import *

def inicio():
    Usuario.recuperarUsuarios()
    for u in Usuario.lista:
        print(u)
        print("\n")

def crearNuevoUsuario():
    nombre = 'Simon'
    apodo = 'saimon'
    correo = 'simon@gmail.com'
    contrasenia = '12345'
    nuevoUsuario = Usuario(
        id=None,
        nombre=nombre,
        apodo=apodo,
        correo=correo,
        contrasenia=contrasenia
    )
    Usuario.guardarNuevoUsuario(nuevoUsuario)

inicio()
crearNuevoUsuario()
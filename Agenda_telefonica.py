#agregarcontactos
#Remover contactos
#Actualizar Contactos
#Ver contacto
#Ver todos los contactos

Diccionario_agenda = dict()


def plantilla(nombre_operacion):
    print("\n", "-----------Agenda Telefonica del futuro-----------")
    print(nombre_operacion)
    print("--------------------------------------------------", "\n")


def Agregar_contacto():
    print("\n")
    nombre = input("Nombre del nuevo contacto: ")
    telefono = input("Telefono del nuevo contacto: ")
    Diccionario_agenda[nombre.capitalize()] = telefono
    plantilla("Contacto Agregado")


def Remover_contacto():
    print("\n")
    nombre = input("Ingrese el nombre del contacto a borrar: ")
    try:
        del Diccionario_agenda[nombre.capitalize()]
        plantilla("Contacto Borrado!!!!!")
    except KeyError:
            plantilla("Nombre Invalido!!!!!!")


def Actualizar_contacto():
    contacto = input("Nombre que desea actualizar el numero: ")
    telefono = int(input("Telefono nuevo: "))
    try:
        Diccionario_agenda[contacto.capitalize()]
    except (ValueError, KeyError):
        plantilla("Error numero solo se aceptan numeros: ")
        plantilla("Regresando al menu de agenda telefonica del futuro")
    else:
        Diccionario_agenda[contacto.capitalize()] = telefono
        plantilla("Actualizado con exito!!!!!!!!!!!!!!!")


def Ver_contacto():
    print("\n")
    contacto = input("Escriba el nombre: ")
    try:
        print("\n")
        contacto = contacto.capitalize()
        print(contacto, "-", Diccionario_agenda[contacto.capitalize()])
    except KeyError:
        plantilla("Contacto no Existe")


def Ver_todo():
    nombre_operacion = "None"

    for contacto in Diccionario_agenda:
        nombre_operacion += "\n {} - {}".format(contacto, Diccionario_agenda[contacto])
            
    if len(Diccionario_agenda) == 0:
        nombre_operacion = "Ningun contacto Registrado"
    plantilla(nombre_operacion)


plantilla("+++++++++++Bienvenido+++++++++++")

while True:
    try:
        print("1- Agregar contacto")
        print("2- Remover contacto")
        print("3- Actualizar contacto")
        print("4- Ver contacto especifico")
        print("5- Ver todos")
        print("6- Salir")
        operacion = int(input(":"))
        if operacion == 1:
            Agregar_contacto()
        elif operacion == 2:
            Remover_contacto()
        elif operacion == 3:
            Actualizar_contacto()
        elif operacion == 4:
            Ver_contacto()
        elif operacion == 5:
            Ver_todo()
        elif operacion == 6:
            break
        else:
            plantilla("Operacion Desconocida solo numeros del 1 al 6")
    except ValueError:
        plantilla("Error de Usuario. solo se aceptan numeros del 1 al 6")
    else:
        pass

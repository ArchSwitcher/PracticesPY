#obtiene los sets del usuario los llamaremos a y b
#devemos hacer funcion de union
#devemos hacer funcion de interseccion
#devemos hacer funcion de diferencia
#devemos hacer funcion de diferencia simetrica
def plantilla(mensaje):
    print("\nBienvenido a la operacion de conjuntos python \n \n")
    print(mensaje)
    print("--------------------------------------------------","\n")


def Union_conjuntos(conjunto_a,conjunto_b):
    plantilla("++++UNION++++ \n \n \n La union de a y b es {}\n \n".format(conjunto_a.union(conjunto_b)))


def Interseccion_conjuntos(conjunto_a, conjunto_b):
    plantilla("++++Intersección ++++ \n \n \n La interseccion de a y b es {}\n \n".format(conjunto_a.intersection(conjunto_b)))


def Diferencia_conjunto(conjunto_a,conjunto_b):
    Diferencia=int(input("++++Diferencia ++++ \n \n \n Desea restar los conjuntos\n 1- (Conjunto_a-Conjunto_b)\n 2- (Conjunto_b-Conjunto_a)"))
    try:
        if Diferencia == 1:
            plantilla("Conjunto_a - Conjunto_b es = {}\n \n".format(conjunto_a.difference(conjunto_b)))
        elif Diferencia == 2:
            plantilla("Conjunto_b - Conjunto_a es = {}\n \n".format(conjunto_b.difference(conjunto_a)))
    except ValueError:
        print("solo se aceptan numeros del 1 al 2")
    
    
def Diferencia_simetrica_conjuntos(conjunto_a,conjunto_b):
    plantilla("+++++Difrencia simetrica +++++ \n \n \n  conjunto_a - conjunto_b es =  {} \n \n ".format(conjunto_a.symmetric_difference(conjunto_b)))
    

def Instructivo():
    print("4- Union","\n","5- Interseccion","\n","6- Diferencia","\n","7- Diferencia Simetrica","\n"," 8- Ingresar nuevos conjuntos\n", "9- Atras")


def operaciones(Conjunto_a,Conjunto_b,operacion):
    if operacion == 4:
        Union_conjuntos(Conjunto_a,Conjunto_b)
    elif operacion == 5:
        Interseccion_conjuntos(Conjunto_a, Conjunto_b)
    elif operacion == 6:
        Diferencia_conjunto(Conjunto_a,Conjunto_b)
    elif operacion == 7:
        Diferencia_simetrica_conjuntos(Conjunto_a,Conjunto_b)
    elif operacion == 8:
        plantilla("\n***********ingresar nuevos conjuntos?***********\n")
        Calculadora_de_conjuntos()
    elif operacion == 9:
        plantilla("\n***********Regresando al menu principal?***********\n")
        pass


def Calculadora_de_conjuntos():
    print("Bienvenido a los conjuntos", "\n", "introduce los elementos de los conjuntos separados por espacios", "\n", "Ejemplo: 1 3 5 6 8 9") 
    
    conjunto_a =  set(input("conjunto A:").rsplit())
    conjunto_b =  set(input("conjunto B:").rsplit())

    #print("ahora porfavor ingresa el comando que deseas realizar","\n" )

    while True:
        #print("ahora por favor ingresa el comando que deseas realizar","\n","1- Union","\n","2- Interseccion","\n","3- Diferencia","\n","4- Diferencia Simetrica","\n","6- salir")
        print("ingresa 1 para ver operaciones disponibles, 2 para ver conjuntos ingresados y 3 para salir ")
        
        try:
            operacion= int(input(":" ))
        except ValueError:
            print("1- Ver instructivo","\n","2- Ver Conjuntos ingresados","\n","3- Salir")
        else:
            if operacion == 1:
                Instructivo()
            elif operacion == 2:
                print("conjunto A: ",conjunto_a)
                print("conjunto B: ",conjunto_b)
            elif operacion == 3:
                print("Devera ingresar los conjuntos nuevamente?")
                break
            elif operacion > 3:
                operaciones(conjunto_a,conjunto_b,operacion)
            else:
                print("numero mayor a 8 ingrese un numero entre 1 y 8")


    continuar = input("Desea continuar realizando operaciones?   si/no: ")
    if continuar == "si":
        Calculadora_de_conjuntos()
    else:
        pass


Calculadora_de_conjuntos()
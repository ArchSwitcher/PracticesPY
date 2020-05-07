#5 vidas por juego
#Pistas del numero si es mayor o menor
#Opcion de volver a jugar
#facil numeros del 0 al 10 con ayuda
#medio numeros del 0 al 40 con ayuda
#dificil reducir el numero de intentos
import random


def Plantilla(mensaje):
    print("\n","!!!!!Adivina el numero!!!!!")
    print(mensaje)
    print("+++++++++++++++++++++++++++", "\n")


def jugar():
    
    print("+++++++++++++++Bienvenido+++++++++++++++")
    print("1- Facil","\n","2- Medio","\n","3- Dificil")
    
    try:
        respuesta = int(input(": "))
        if respuesta == 1:
            intentos = 5
            inicio_random = 0
            fin_random = 10
        elif respuesta == 2:
            intentos = 5
            inicio_random = 0
            fin_random= 50
        elif respuesta == 3:
            intentos = 3
            inicio_random = 0
            fin_random = 10
       
    except ValueError:
        Plantilla("Solo Numeros por favor: ")
    
    Numero_aleatorio = random.randint(inicio_random,fin_random)
    nombre_operacion = "trata de adivinar los numeros del {} al {} con vidas {}".format(inicio_random,fin_random,intentos)
    Plantilla(nombre_operacion)
    
    
    while intentos > 0:
        adivinanza = int(input("Ingresa un numero entre {} y {}: ".format(inicio_random, fin_random)))

        if adivinanza > fin_random:
            Plantilla("Ingresa un numero entre {} y {}".format(inicio_random, fin_random))

        elif adivinanza == Numero_aleatorio:
            ganaste = "Felicidades Ganste. el numero ganador fue {}".format(adivinanza)
            Plantilla(ganaste)
            break

        else:
            nombre_operacion = None
            if Numero_aleatorio<adivinanza:
                ayuda = "El numero es menor te quedan"
            else:
                ayuda = "El numero es mayor te quedan"
        
            intentos-=1
            nombre_operacion = "{} te quedan {} vidas. el numero que ingresate es: {}".format(ayuda,intentos,adivinanza)
            Plantilla(nombre_operacion)
            Plantilla("fallaste")
            

    volver = input("volver a jugar: ")
    if volver == "si":
        jugar()
    
jugar()      


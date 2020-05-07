#EJEMPLO DE WHILE
manzanas  =10
while manzanas >0:
    print("manzanas restantes "+ str(manzanas))
    manzanas -=1

#EJEMPLO DE FOR
lista_numeros = [1,    2,    3,    4,    5,    6,    7,    8,    9,    10]

for numero in lista_numeros:
    if numero > 5:
        print("ciclo Roto")
        break
    print(str(numero))
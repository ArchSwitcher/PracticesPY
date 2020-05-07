def operacion(res, num1, num2):
    if res == 1:
      return  num1+num2
    elif res == 2:
       return  num1-num2
    elif res == 3:
       return  num1*num2
    elif res == 4:
       return  num1/num2

print("Bienvenido a la calculadora","\n","Estas operaciones puedes utilizar")
while True:
    try:
        print("1- Suma","\n","2- Resta","\n","3- Multiplicacion","\n","4- Division" )
        res = int(input("Que operacion desea realizar? "))
        num1 = int(input("Ingrese el primer numero "))
        num2 = int(input("Ingrese el primer numero "))
        
    except ValueError:
        print("Solo se aceptan numeros no letras")
    else:
        if res < 1 or res > 4:
            print("\n","ese no es un numero valido","\n")
            continue
        total = operacion(res,num1,num2)
        print("la respuesta es = ", str(total))
        res = input("Desea continuar si/no = ")
        if res != "si":
            break

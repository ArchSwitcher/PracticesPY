import re
break2 = True

def Add_items(items):
    items_add = open("super_app!","a")
    items_add.write("{}\n".format(items))

def See_items():
    items_file = open("super_app!",encoding="utf-8")
    info = items_file.read()
    items_file.close()
    print(info)

def functions(*string):
    string = input("menu salir:" )  
    if string == "Salir111":
        return 1
        
    elif string == "menu":
        main()

def main():
    
    print("Bienvenido a un notepad basico xD")
    print(" 1- Salir \n 2- Ver notepad \n 3- Escribir en él notepad \n     para salir del programa escriba Salir111  para el menu lo mismo")
    operacion = int(input(": "))
    print(operacion)

    while break2:
        if operacion == 1:
            break
        elif operacion == 2:
            See_items()
            operacion = functions()
        elif operacion == 3:
            string = input(":")
            Add_items(string)
            if string == "Salir111":
                operacion = functions("Salir111")
            
                
main()
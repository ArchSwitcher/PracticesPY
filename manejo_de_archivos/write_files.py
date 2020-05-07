def Add_item(items):
    fille_list = open("file_list","a")  #Generando archivo si existiera lo abre la w es para decir que podemos escribir en él existen mas modos en la doc python
    fille_list.write("{}\n".format(items))
    fille_list.close()

Add_item(input("Escribe lo que quieres se esta guardando en un kate!!: "))
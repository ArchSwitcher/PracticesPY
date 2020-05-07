import datetime
now = datetime.datetime.now()

now.strftime("%B %d, %Y  %I:%M:%S:%f")   # se genera una cadena apartir de una hora y fecha

fecha_cadena = "06/01/2020"
fecha_formato = datetime.datetime.strptime(fecha_cadena,"%d/%m/%Y")   #espera la cadena y la extrae en este caso fecha_cadena debe contener el mismo formato es decir si usamos numeros no podemos decirle que los convierta a su equivalente en dia o mes

print(fecha_formato)

#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
#para encontrar la tabla donde estan todos demas codigos con busqueda de navegador obio xD strftime

# https://strftime.org/ link donde se encuentran de forma directa 

# TODO: colocar el formato como MONDAY, February, 6, 2017 10:47:04 pm (12)
# TODO: colocar formato hora como 10:47:04 pm (12)
import datetime


def Instructions():
    print("Bienvenido a reloj del mundo")
    print("operaciones que puedes realizar")
    print("1- Ver la hora \n 2- Ver la fecha hora \n 3- Ver la hora en Nueva York \n 4- ver la hora en San Fransico \n 5- ver hora Bucharest-Romania\n 6- Guam \n 7- ver instrucciones \n 8- Salir")


def see_hour(time_zones = -6, place = "Zona central"):
    sformat = "%-I:%M:%S %p"
    time_zone = datetime.timezone(datetime.timedelta(hours=+ time_zones))
    actual_time = datetime.datetime.now(time_zone).time()
    format_time = actual_time.strftime(sformat)
    print("El formato UTC  {}  es {} \n {}".format(time_zones,format_time,place))

def see_hour_date():
    sformat = "%A, %B, %d, %Y, %-I:%M:%S %p"
    time_zone = datetime.timezone(datetime.timedelta(hours=-6))
    print(time_zone)
    actual_date_time = datetime.datetime.now(time_zone)
    print(actual_date_time)
    format_time_date = actual_date_time.strftime(sformat)
    print("la fecha y hora de UTC-6 para Guatemala es {} ".format(format_time_date))


def see_hour_date1():
    time_zone = datetime.timezone(datetime.timedelta(hours=-6))
    fecha_hora_actual = datetime.datetime.now(time_zone)
    print(fecha_hora_actual)


def see_watch():
    Instructions()
    while True:
        operation = int(input(": "))
        
        if operation == 1:
            print("\n \n")
            see_hour()
        elif operation == 2:
            print("\n \n")
            see_hour_date()
        elif operation == 3:
            print("\n \n Hora en Nueva York")
            see_hour(-5,"zona del pacifico")
        elif operation == 4:
            print("Hora en San Fransisco")
            see_hour(-8,"Zona del este")
        elif operation == 5:
            print(" \n \nHora en Bucharest-Romania")
            see_hour(2,"Zona Bravo")
        elif operation == 6:
            print("\n \n Hora en Guam")
            see_hour(10,"Zona del Pacifico")
        elif operation == 7:
            print(" \n \n Ver instrucciones")
            Instructions()
        elif operation == 8:
            break
        else:
            print("solo numeros del 1 al 8")
        
see_watch()
Instructions()

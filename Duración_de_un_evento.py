


hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))


#Definir minutos totales
 # 1. Sumo los minutos + la duración del evento.
 # 2. del total saco el modulo. Una divisón normal, me daria como resultado
 #    en el cociente la parte entera, esta seia mi  cantidad de horas
 #    el modulo en cambio, me muestra lo que sobró, que en este caso son los minutos
 #    que en este caso serian los minutos. 
minTotal = (min + dura)%60  


#Definir horas totales
# 1. Sumo los minutos + la duración del evento y hago una division entera.
#    la división entera, me muestra la cantidad de horas 
# 2. Ese valor lo sumo a la hora de inicio del evento, lo cual me da
#    el total de horas que duraria el evento.
# 3. A ese total de horas, le saco el modulo. 
#    este proceso deja por fuera la parte entera, que en este caso serían
#    los días totales, y me deja como resultado, la hora final del evento
horaTotal = (((min + dura)//60) + hora)%24

 

print("El eventó terminará a las: ", horaTotal, ":", minTotal)


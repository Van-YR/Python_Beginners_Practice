
def CDT(usuario:str, capital:int, tiempo:int):
    
    if tiempo < 0:
        tiempo = tiempo * (-1)
    if tiempo > 2:
        porcentaje = 0.03
        interes = ((capital * porcentaje) * tiempo) /12
        valorTotal = capital + interes 
    else:
        porcentaje = 0.02
        interes = (capital * porcentaje)
        valorTotal = capital - interes 
    
    return  (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}")



#Sistema de Control Vacacional
print("===================================")
print("SISTEMA DE CONTROL VACACIONAL RAPPI")
print("===================================")

nombre_empleado = input("\n Por favor ingrese el nombre del empleado: ")

clave_departamento = int(input("Por favor ingrese la clave del departamento: "))

antiguedad_empleado = float(input("Por favor ingrese la cantidad de años de servicio: "))

if clave_departamento == 1:
    print("\n *** Departamento: Atención al cliente*** ")
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("\n El trabajador ", nombre_empleado, " tiene derecho a 6 días de vacaciones")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("\n El trabajador ", nombre_empleado, " tiene derecho a 14 días de vacaciones")
    elif antiguedad_empleado >= 7:
        print("\n El trabajador ", nombre_empleado, " tiene derecho a 20 días de vacaciones")
    else:
        print(" \n El trabajador ", nombre_empleado, "aún no tiene derecho a vacaciones.")

elif clave_departamento == 2:
    print("\n ***Departamento: Logística*** ")
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("\n El trabajador ", nombre_empleado, " tiene derecho a 7 días de vacaciones")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("\n El trabajador ", nombre_empleado, " tiene derecho a 15 días de vacaciones")
    elif antiguedad_empleado >= 7:
        print("\n El trabajador ", nombre_empleado, " tiene derecho a 22 días de vacaciones")
    else:
        print(" \n El trabajador ", nombre_empleado, "aún no tiene derecho a vacaciones.")
        
elif clave_departamento == 3:
    print("\n ***Departamento: Gerencia*** ")
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("\n El trabajador ", nombre_empleado, " tiene derecho a 10 días de vacaciones")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("\n El trabajador ", nombre_empleado, " tiene derecho a 20 días de vacaciones")
    elif antiguedad_empleado >= 7:
        print("\n El trabajador ", nombre_empleado, " tiene derecho a 30 días de vacaciones \n")
    else:
        print(" \n El trabajador ", nombre_empleado, "aún no tiene derecho a vacaciones.")
else:
    print("\n La clave que ha ingresado no existe, por favor verifique la información.")


    

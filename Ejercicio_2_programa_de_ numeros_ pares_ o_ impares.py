print("******************************************************")
print("* Programa que determina si un número es par o impar *")
print("******************************************************")

numero_uno = int(input("\n Por favor introduce un número entero: "))
numero_dos = 2

operacion = numero_uno % numero_dos

if operacion == 0:
    print("El número", numero_uno, " es par.")

elif operacion == 1:
    print("El número", numero_uno, " es impar.")


# otra opción de solución para el ejercicio

print(" \n******************************************************")
print("* Programa 2 que determina si un número es par o impar *")
print("******************************************************")

numero = int(input("\n Por favor introduce un número entero: "))

if numero % 2 == 0:
    print("El número", numero, " es par.")

elif numero % 2 == 1:
    print("El número", numero, " es impar.")

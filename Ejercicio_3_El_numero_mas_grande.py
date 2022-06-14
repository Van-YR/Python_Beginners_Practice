# Clase No. 18 - Ejercicio práctico No. 3

# Solución propia:

print("***************************************************************************")
print("* Programa para determinar ¿Cuál es el número más grande de tres números? *")
print("***************************************************************************")

num_uno = int(input("\nIntroduce el primer número: "))
num_dos = int(input("Introduce el segundo número: "))
num_tres = int(input("Introduce el tercer número: "))

if num_uno > num_dos and num_uno > num_tres:
    print("El número ", num_uno, "  es el número más grande de los tres.")

elif num_dos > num_uno and num_dos > num_tres:
    print("El número ", num_dos, "  es el número más grande de los tres.")

elif num_tres > num_dos and num_tres > num_uno:
    print("El número ", num_tres, "  es el número más grande de los tres.")

elif num_uno == num_dos and num_dos == num_tres:
    print("Todos los numeros son iguales")


# Solución propuesta:

print("\n***************************************************************************")
print("* Programa para determinar ¿Cuál es el número más grande de tres números? *")
print("***************************************************************************")

num_uno = int(input("\nIntroduce el primer número: "))
num_dos = int(input("Introduce el segundo número: "))
num_tres = int(input("Introduce el tercer número: "))

if num_uno > num_dos and num_uno > num_tres:
    print("El número ", num_uno, "  es el número más grande de los tres.")
else:
    if num_dos > num_tres:
        print("El número ", num_dos, "  es el número más grande de los tres.")
    else:
        print("El número ", num_tres, "  es el número más grande de los tres.")
        

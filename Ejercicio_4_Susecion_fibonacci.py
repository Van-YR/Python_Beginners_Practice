# Secuencia de Fibonacci

# Solución personal propuesta con 7 lineas de código

num_uno = 0
num_dos = 1

    
while num_uno < 1597:
    print(num_uno, end=" ")
    num_uno += num_dos
    
    print(num_dos, end=" ")
    num_dos += num_uno


#Aqui termina el código propuesto
    
print(" \n")

# Solución aprendida con 5 lineas de código

num_uno, num_dos = 0, 1

while num_dos <= 1597:
    print(num_uno, num_dos, end=" ")
    num_uno = num_uno + num_dos
    num_dos = num_dos + num_uno
 

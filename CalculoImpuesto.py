
ingreso=float(input("Ingrese el ingreso anual:"))
excencion = 556.2

if ingreso < 85528:
    impuesto = (ingreso * 0.18) - excencion
else:
    impuesto = ((ingreso - 85528)*0.32) + 14839.2

if impuesto <1.0:
    impuesto = 0


impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")

valor = int(input("Introduce un valor: "))
valor2 = int(input("Introduce un segundo valor: "))

if valor > valor2:
    valorGran = valor
elif valor == valor2:
    print("Los dos valores son iguales")
else:
    valorGran = valor2

print("El valor mas grande es: " + str(valorGran))

valor = int(input("Introduce un valor en euros: "))

while valor:
    iva = int(input("Introduce el IVA a aplicar (4, 10 o 21): "))
    if iva == 4:
        break
    elif iva == 10:
        break
    elif iva == 21:
        break
    else:
        print("El IVA introducido no es válido. Debe ser 4, 10 o 21.")

resultadoFinal = valor * (iva / 100)
valorConIva = valor + resultadoFinal

print("Valor sin IVA: " + str(valor) + " €")
print("IVA a aplicar: " + str(iva) + "%")
print("Valor con IVA añadido: " + str(valorConIva) + " €")

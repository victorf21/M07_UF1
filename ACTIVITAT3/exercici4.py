numeros = input("Introduce 10 numero separados por espacio: ")

cadena = numeros.split()

cadena = [int(num) for num in cadena]

tupla = tuple(sorted(cadena))

print(tupla)
numeros = input("Introduce 10 números separados por espacios: ")

cadena = numeros.split()

cadena = [int(num) for num in cadena]

tupla = tuple(sorted(cadena))

print(tupla)
while True:
    numero = int(input("Introduce un número entre 10 y 100: "))
    if 10 <= numero <= 100:
        tupla = tuple(range(1, numero + 1))
        print(tupla)
    else:
        print("Por favor, introduce un número entre 10 y 100.")
        

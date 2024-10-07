while True:
    numero = int(input("Introduce un número entre 1 y 10: "))
    if 1 <= numero <= 10:
        tablaMult = tuple((value * numero for value in range(1,11)))
        print(tablaMult)
        break
    else:
        print("Por favor, introduce un número entre 1 y 10.")
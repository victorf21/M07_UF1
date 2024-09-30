entrada = input("Introduce entre 1 y 3 palabras: ")

palabras = entrada.split()

if 1 <= len(palabras) <= 3:
    for paraula in palabras:
        
        numCaracter = len(paraula)
        primerCaracter = paraula[0]
        ultimoCaracter = paraula[-1]
        
        print("Palabra: " + paraula)
        print("Número de caràcters: " + str(numCaracter))
        print("Primer caràcter: " + str(primerCaracter))
        print("Últim caràcter: " + str(ultimoCaracter))

else:
    print("Tienes que introducir entre 1 y 3 palabras")

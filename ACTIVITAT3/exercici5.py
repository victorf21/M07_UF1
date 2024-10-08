frase = input("Introduce una frase: ")

noEspais= frase.replace(" ", "")

tupla = tuple(noEspais)

caractersNoRepetits = "".join(sorted(set(noEspais), key=noEspais.index))

print(tupla)

print(caractersNoRepetits)

frase = input("Introduce una frase: ")

noEspais= frase.replace(" ", "")

tupla = tuple(noEspais)

caractersNoRepetits = ""
for caracter in noEspais:
    if caracter not in caractersNoRepetits:
        caractersNoRepetits += caracter

print(tupla)

print(caractersNoRepetits)

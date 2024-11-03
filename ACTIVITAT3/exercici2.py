meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
while True:
    numero = int(input("Introduce un número entre 0 y 12: "))
    if numero == 0:
        break
    elif 1 <= numero <=12:
        mesUsuario = meses[numero - 1]
        print(mesUsuario)
    else:
        print("Introduce un número correcto")
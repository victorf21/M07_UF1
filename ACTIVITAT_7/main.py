from create import create_users
from read import read_users
from update import update_users
from delete import delete_user

def main():
    # Menú de las opciones CRUD
    print("--- Menú CRUD ---\n")
    print("1. Crear usuario")
    print("2. Leer usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario\n") 
    # Solicita al usuario que seleccione una opción
    opcio = int(input("Selecciona una opción: "))
    # Ejecuta la opción seleccionada
    if opcio == 1:
        create_users()
    elif opcio == 2:
        read_users()
    elif opcio == 3:
        update_users()
    elif opcio == 4:
        delete_user()
    else:
        print("Opción no válida. Inténtalo de nuevo.")

main()
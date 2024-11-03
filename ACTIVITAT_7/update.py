from connection import get_connection
import psycopg2

def update_users():
    # Solicita el ID del user a modificar y sus nuevos datos
    user_id = int(input("Introduce el ID del usuario que quieres actualizar: "))
    name = input("Introduce el nuevo nombre: ")
    surname = input("Introduce el nuevo apellido: ")
    age = int(input("Introduce la nueva edad: "))
    email = input("Introduce el nuevo email: ")
    telefon = input("Introduce el nuevo teléfono: ")
    try:
        conn, connection = get_connection() # Conexión a la base de datos
        # Query para actualizar un usuario
        sql = '''
            UPDATE USERS
            SET user_name = %s, user_surname = %s, user_age = %s, user_email = %s, user_telefon = %s
            WHERE user_id = %s
        '''
        # Ejecuta la query para actualizar el user según los datos ingresados
        connection.execute(sql, (name, surname, age, email, telefon, user_id))
        # Comprueba si el id del user existe
        if connection.rowcount == 0:
            print(f"No existe ningún usuario con el ID: {user_id}.")
        else:
            conn.commit() # Guarda los cambios realizados en la base de datos
            print("Usuario actualizado correctamente.")
    except (Exception, psycopg2.Error) as error:
        # Manejo de errores 
        print("Error al actualizar el usuario: ", error)
    finally:
        # Cierra la conexión a la base de datos
        connection.close()
        conn.close()
from connection import get_connection
import psycopg2

def delete_user():
    # Solicita el ID del usuario a eliminar
    user_id = int(input("Introduce el ID del usuario que quieres eliminar: "))
    try:
        conn, connection = get_connection() # Conexión a la base de datos
        sql = "DELETE FROM USERS WHERE user_id = %s" # Query para borrar un usuario con el ID proporcionado
        connection.execute(sql, (user_id,)) # Ejecuta la query con el ID proporcionado
        # Comprueba si el id del user existe
        if connection.rowcount == 0:
            print(f"No existe ningún usuario con el ID: {user_id}." )
        else:
            conn.commit() # Guarda los cambios realizados en la base de datos
            print("Usuario eliminado correctamente.")
    except (Exception, psycopg2.Error) as error:
        # Manejo de errores
        print("Error al eliminar el usuario: ", error)
    finally:
        # Cierra la conexión a la base de datos
        connection.close()
        conn.close()
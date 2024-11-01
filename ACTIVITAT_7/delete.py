from connection import get_connection
import psycopg2

def delete_user():
    user_id = int(input("Introduce el ID del usuario que quieres eliminar: "))
    try:
        conn, connection = get_connection()
        sql = '''
            DELETE FROM USERS WHERE user_id = %s
        '''
        connection.execute(sql, (user_id,))
        if connection.rowcount == 0:
            print(f"No existe ningún usuario con el ID: {user_id}." )
        else:
            conn.commit()
            print("Usuario eliminado correctamente.")
    except (Exception, psycopg2.Error) as error:
        print("Error al eliminar el usuario: ", error)
    finally:
        connection.close()
        conn.close()

delete_user()
from connection import get_connection
import psycopg2

def update_users():
    user_id = int(input("Introduce el ID del usuario que quieres actualizar: "))
    
    try:
        conn, connection = get_connection()
        # Solicitar datos nuevos para la actualización
        name = input("Introduce el nuevo nombre: ")
        surname = input("Introduce el nuevo apellido: ")
        age = int(input("Introduce la nueva edad: "))
        email = input("Introduce el nuevo email: ")
        telefon = input("Introduce el nuevo teléfono: ")
        
        sql = '''
            UPDATE USERS
            SET user_name = %s, user_surname = %s, user_age = %s, user_email = %s, user_telefon = %s
            WHERE user_id = %s
        '''
        
        # Ejecutar la consulta de actualización
        connection.execute(sql, (name, surname, age, email, telefon, user_id))
        
        # Verificar si alguna fila fue afectada
        if connection.rowcount == 0:
            print(f"No existe ningún usuario con el ID: {user_id}.")
        else:
            conn.commit()
            print("Usuario actualizado correctamente.")
    except (Exception, psycopg2.Error) as error:
        print("Error al actualizar el usuario: ", error)
    finally:
        connection.close()
        conn.close()

update_users()

from connection import get_connection
import psycopg2

def create_users():
    name = input("Introduce el nombre: ")
    surname = input("Introduce el apellido: ")
    age = int(input("Introduce la edad: "))
    email = input("Introduce el email: ")
    telefon = input("Introduce el teléfono: ")
    
    try:
        conn, connection = get_connection()
        sql = '''
            INSERT INTO USERS (user_name, user_surname, user_age, user_email, user_telefon)
            VALUES (%s, %s, %s, %s, %s)
        '''
        connection.execute(sql, (name, surname, age, email, telefon))
        conn.commit()
        print("Usuario creado correctamente.")
    except (Exception, psycopg2.Error) as error:
        print("Error al crear usuario: ", error)
    finally:
        connection.close()
        conn.close()

create_users()
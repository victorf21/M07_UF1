from connection import get_connection
import psycopg2

def create_users():
    # Solicita los datos para el nuevo user
    name = input("Introduce el nombre: ")
    surname = input("Introduce el apellido: ")
    age = int(input("Introduce la edad: "))
    email = input("Introduce el email: ")
    telefon = input("Introduce el teléfono: ")
    
    try:
        # Conexión a la base de datos
        conn, connection = get_connection()
        # Query para insertar nuevo user
        sql = '''
            INSERT INTO USERS (user_name, user_surname, user_age, user_email, user_telefon)
            VALUES (%s, %s, %s, %s, %s)
        '''
        # Ejecuta la query para insertar un nuevo user según los datos ingresados
        connection.execute(sql, (name, surname, age, email, telefon))
        conn.commit() # Guarda los cambios realizados en la base de datos
        print("Usuario creado correctamente.")
    except (Exception, psycopg2.Error) as error:
        # Manejo de errores
        print("Error al crear usuario: ", error)
    finally:
        # Cierra la conexión a la base de datos
        connection.close()
        conn.close()
from connection import get_connection
import psycopg2

def create_table_users():
    try:
        conn, connection = get_connection() # Conexión a la base de datos
        # Query para crear tabla
        sql = ''' 
            CREATE TABLE IF NOT EXISTS USERS(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                user_surname VARCHAR(255) NOT NULL,
                user_age BIGINT NOT NULL,
                user_email VARCHAR(255) NOT NULL,
                user_telefon VARCHAR(15)
            )
        '''
        connection.execute(sql) # Ejecuta la query
        conn.commit() # Guarda los cambios realizados en la base de datos
        print("Tabla creada correctamente.")
    except (Exception, psycopg2.Error) as error:
        # Manejo de errores
        print("Error al crear la tabla: ", error)
    finally:
        # Cierra la conexión a la base de datos
        connection.close()
        conn.close()
        
create_table_users()
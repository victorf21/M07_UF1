import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='user_postgres',
            password='pass_postgres',
            host='localhost', 
            port='5432'
        )
        connection = conn.cursor()
        return conn, connection
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None, None

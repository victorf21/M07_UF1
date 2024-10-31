from connection import get_connection
import psycopg2

def read_users():
    try:
        conn, connection = get_connection()
        sql = "SELECT * FROM USERS"
        connection.execute(sql)
        users = connection.fetchall()
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error al leer los usuarios:", error)
    finally:
        connection.close()
        conn.close()
    return users

read_users()
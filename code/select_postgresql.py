import psycopg2
from conn_postgresql import conexion

try:
    with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT * FROM happiness limit 10;")
        # Hacer un while, mientras fetchone no regrese None
        happiness = cursor.fetchone()
        while happiness:
            print(happiness)
            happiness = cursor.fetchone()
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()
import psycopg2
import os

#Cargo los datos de la conexion con mi base postgresql
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")

credenciales={
    "dbname": "database",
    "user": POSTGRES_USER,
    "password": POSTGRES_PASSWORD,
    "host": "db",
    "port": DB_PORT
}

try:
    conexion = psycopg2.connect(**credenciales)
    print("conexion establecida")
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)
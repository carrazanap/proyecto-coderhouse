import pandas as pd
from sqlalchemy import create_engine
import os

#Cargo los datos de la conexion con mi base postgresql
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")

#Creo conexion con la base de datos  
conn_string = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:{DB_PORT}/{POSTGRES_DB}'
  
db = create_engine(conn_string)
conn = db.connect()

# Load DataFrame
df_happiness = pd.read_csv('./data/Happiness_final.csv')
# Creo la tabla con la informacion del dataframe
df_happiness.to_sql('happiness', con=conn, if_exists='replace',
          index=False)
#conn.commit()
#conn.close()
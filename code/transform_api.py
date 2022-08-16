import pandas as pd
import requests
import json
import time
import numpy as np

#Carga dateset
df_happiness = pd.read_csv('./data/Happiness_union.csv')

#Creo una funcion donde paso por parametro el nombre del pais y la API me devuelto latitud y longitud
def api_requests(country:str):
    requests_api = f"https://nominatim.openstreetmap.org/search.php?country={country}&dedupe=0&format=jsonv2"
    response = requests.get(requests_api)
    if  len(response.json()) == 0: 
        return np.nan,np.nan
    else: 
        return response.json()[0]['lat'], response.json()[0]['lon']


#Aplico la funcion creada a cada fila del dataframe y agrego latitud y longitud como columnas
inicio = time.time()
df_happiness["latitud"],df_happiness["longitud"] = zip(*map(api_requests, df_happiness['Country']))
fin = time.time()
print(fin-inicio)
#1060 seg = 17 min

#Cantidad filas,cantidad columnas
print(f'Cantidad filas: {df_happiness.shape[0]} \nCantidad columnas: {df_happiness.shape[1]}')

#Borro un pais xx
df_happiness = df_happiness.query("Country != 'xx'").copy()

#Exporto el dataframe final a .csv
df_happiness.to_csv('./data/Happiness_final.csv',index=False)
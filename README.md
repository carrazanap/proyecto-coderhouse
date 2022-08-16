# Proyecto Coderhouse 🚀
 
El objetivo del proyecto es la carga de archivos y transformarlos para posteriormente insertarlos en una tabla en postgresql y en un bucket de AWS S3. Finalmente mostrar visualizaciones analizando los datos.
 
# Datasets 📕
 
Informe mundial de la felicidad: Ranking mundial de la felicidad basado en distintos índices
```
https://www.kaggle.com/datasets/mathurinache/world-happiness-report
```
API Nominatim: API que te brinda la geolocalización de una dirección, localidad o país
```
https://nominatim.org/release-docs/latest/
```
 
# Arquitectura 👷‍♂️

![arq_it](https://user-images.githubusercontent.com/17929994/184785715-73172544-1be7-4842-bd5e-6aa200ae7ab7.jpg)
 
Estructura de archivos

![arq_folder](https://user-images.githubusercontent.com/17929994/184785804-f4c99f5a-69e2-4506-90e1-e4d66c3e5713.jpg)
 
# Instalar y ejecutar 🔧
 
Primero se requiere crear un archivo .env con las siguientes variables para ejecutar `docker` con los servicios de python y postgresql
 
```
AWS_ACCESS_KEY=XXXXXXXXXXXXX
AWS_SECRET_KEY=XXXXXXXXXXXXXXXX
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
DB_PORT=5433
JUPYTER_ENABLE_LAB=yes
JUPYTER_TOKEN=coderhouse
```
Ejecutar docker
```
$ docker-compose up --build -d
```
Puedo validar que se están ejecutando con el siguiente comando
```
$ docker ps
```
![docker_ps](https://user-images.githubusercontent.com/17929994/184785851-e56051b1-b690-45b4-81b9-10f55d1eb49b.jpg)

## Ingreso al bash para ejecutar cada archivo python por separado
```
$ docker exec -it coderhouse_app bash
```
 
## Tranformo los archivos csv de cada año y los uno en un solo dataset con algunas transformaciones en las columnas
```
$ python transform_files.py
```
![transform_files](https://user-images.githubusercontent.com/17929994/184785908-67fcf406-3c4e-4c03-b956-bd75ceee7d67.jpg)
 
## Al archivo anterior, agrego el uso de la API Nominatim para agregar latitud y longitud de los diferentes paises
El proceso demora aproximadamente unos 15 min, el archivo Happiness_final.csv ya se encuentra dentro de /files
```
$ python transform_api.py
```
![transform_api](https://user-images.githubusercontent.com/17929994/184785956-f6346b79-36e7-4fe2-b3ac-6ba251790e55.jpg)
 
El proceso demora aproximadamente unos 15 min, el archivo Happiness_final.csv ya se encuentra dentro de /data
 
## Almaceno el dataset en la base de datos Postgresql, el servicio ya se encuentra corriendo
 
Válido que la conexión es correcta
```
$ python conn_postgresql.py
```
![conn_postgresql](https://user-images.githubusercontent.com/17929994/184786025-81627d6b-7de7-4de1-b0bf-02d0afc75ad9.jpg)
 
Cargo el dataset en la tabla happiness
```
$ python load_postgresql.py
```
 
Consulto la tabla y que contenga los datos cargados, en este caso solo muestro 10 registros
```
$ python select_postgresql.py
```
## Almaceno el dataset en AWS S3
 
```
$ python load_s3.py
```
![load_s3](https://user-images.githubusercontent.com/17929994/184786063-0c6b5787-9efc-4593-9e9a-cd6d0f54018b.jpg)
 
Desde la interfaz de AWS se ve de la siguiente manera
 
![aws_s3](https://user-images.githubusercontent.com/17929994/184786105-911dc7d3-bdad-4c91-8707-a799a62b8a3b.jpg)
 
## Visualizaciones 📈
 
El archivo a ejecutar es el siguiente pero ya está corriendo
```
$ python dashboard.py
```
Se puede visualizar en su navegador
```
http://localhost:8052/
```
El primer gráfico es un mapa donde se muestra cada país con sus respectivo Score y también de esto depende el tamaño del punto
 
![dashboard_1](https://user-images.githubusercontent.com/17929994/184786149-8ab63c66-8ac2-4eb2-bb01-f6f4ff2ca067.jpg)
 
En el segundo gráfico es de líneas y se observa los distintos índices, y se puede filtrar por cada país
 
![dashboard_2](https://user-images.githubusercontent.com/17929994/184786179-b56c3b6e-843a-4cef-a451-5745805bdcb4.jpg)
 
## Machine Learning
 
Se corrieron dos modelos LinearRegression y GradientBoostingRegressor, donde el segundo fue el que mejor funcionó dándome un Score más alto en la predicción
```
$ python machine_learning.py
```
![ml](https://user-images.githubusercontent.com/17929994/184786206-e435ce59-c76d-4561-a026-9cd119d2f942.jpg)

## Jupyterlab
 
Si se desea correr el notebook, esta corriendo jupyterlab en el siguiente puerto y el token:coderhouse
```
http://localhost:8888/
```
![jupyter](https://user-images.githubusercontent.com/17929994/184786229-faad10f1-7561-4743-b300-002db66e8d5d.jpg)

## Si se desea se puede entrar al contenedor de la base de datos postgress y validar la tabla
 
```
$ docker exec -it coderhouse_db bash
```
Comando para consultar por la tabla cargada y ver 10 registros
```
$ psql -d postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:${DB_PORT}/database -c "select * from happiness limit 10"
```
![postgresql](https://user-images.githubusercontent.com/17929994/184786261-a5f3d109-bbb5-4106-b9d8-5ac3145c49f5.jpg)

# Conclusión ✒️

Con respecto a lo que fue el dataset, mi hipotesis se confirmo en el analisis y posteriormente en las visualizaciones ya que los paises con un Score de felicidad mas alto son paises europeos, de America del Norte y en Oceanía. Otro punto que me llamo la atencíon fue que un pais potencia como China presento indices bajos.  
El trabajo me llevó a aprender a interactuar con el proceso de ingesta de un archivo .csv en una base de datos y servicio de AWS, después con el agregado de la arquitectura poder llevar esto a Docker y que se pueda ejecutar independientemente del sistema operativo.
Lo que es el modelo de machine learning también fue un aprendizaje.


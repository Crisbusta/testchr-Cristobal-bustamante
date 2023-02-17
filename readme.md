## Contenido del repositorio

El repositorio es un proyecto desarrollado en Django 4 + PostgreSQL + Docker. El uso de docker se debe a la facilidad que tiene docker de instalar dependencias y encapsular todo el proyecto en un contenedor.

El proyecto tiene una sola aplicación llamada testchr, la cual se encarga completamente de la tarea 1 y parcialmente de la tarea 2.

##### Comentarios tarea 1:
En esta tarea me surgieron dudas principalmente sobre cuáles datos manejar del json, finalmente decidí trabajar solo con los datos en 'stations' omitiendo el array 'extras'. 
La función 'save_stations_data' se encarga de obtener los datos de la Api e insertarlos en la base de datos.

Además, realicé los dos items opcionales de la tarea. Creé una vista en el administrador y una vista personalizada que posee una tabla mostrando los datos con paginación incluída, la función 'display_stations_data' se encarga de esto.

##### Comentarios tarea 2:
Esta tarea fue considerablemente más desafiante que la tarea 1. En primer lugar se desarrolla el script 'scraping-proyectos.py' que se encarga de obtener la información de la tabla en la url entregada. 
Todo bien hasta aquí, el problema comienza cuando veo que son 2844 paginaciones y obtener toda la información tardaría demasiado si lo hacía iterando. 
Es por esto que decidí utilizar hilos (Threads) para agilizar la obtención de datos, aún así el script de obtención de datos tarda +10min en obtener toda la información y guardarla en un archivo json.

Para poder insertar toda la data contenida en el json me di la libertad de instalar la librería 'django-import-export' la cual agrega un botón de importación en el administrador de django y nos permite importar masivamente distintos tipos de archivos, entre ellos json.

Con el objetivo de optimizar el tiempo de quién se encargará de probar este proyecto se adjuntan dos archivos json, "tabla_datos.json" posee toda la data extraída del web scraping, en cambio, "test.json" posee solo 20 registros, esto con el propósito de agilizar la importación con fines de pruebas.
Importa el que desees.

Además, realicé los dos items opcionales de la tarea. Creé una vista en el administrador y una vista personalizada que posee una tabla mostrando los datos con paginación incluída, la función 'display_projects_data' se encarga de esto.


## ¿Cómo utilizar este repositorio?
Para ejecutar el proyecto se deben seguir los siguientes pasos:

1. Descargar el repositorio
2. Extraer la carpeta
3. Iniciar docker
4. Abrir la terminal en la ruta donde se extrajo la carpeta
5. Ejecutar el comando ``` docker-compose run web python manage.py makemigrations```
6. Ejecutar el comando ``` docker-compose up --build```
 6.1 Encontré un pequeño bug y no pude solucionarlo 😅 La consola entregará un error al ejecutar ```docker-compose up --build``` por primera vez, simplemente ejecuta el comando de nuevo y el proyecto se ejecutará.
7. Crear un usuario para el admin, ejecutar el comando ``` docker-compose run web python manage.py createsuperuser```
8. Ingresar a la ruta http://localhost:8000/testchr/ (En este momento se obtienen los datos de la Api de la tarea 1 y se insertan en la base de datos)
9. Para ver los datos insertados, ingresar a la ruta: http://localhost:8000/testchr/stations o en su defecto revisar los datos en el admin: http://localhost:8000/admin/testchr/station/
10. Ingresar a la ruta http://localhost:8000/admin/testchr/project/ e importar el archivo json que se encuentra en la raíz del proyecto. El archivo "tabla_datos.json" posee toda la data extraída del web scraping, el archivo "test.json" posee solo 20 registros, esto con el propósito de agilizar la importación con fines de pruebas. Importa el que desees. Pasos para importar:
10.1. ![Descripción de la imagen](https://scontent.fscl11-2.fna.fbcdn.net/v/t39.30808-6/331299149_586945596345508_3168636580135746402_n.jpg?stp=cp6_dst-jpg&_nc_cat=101&ccb=1-7&_nc_sid=730e14&_nc_ohc=iCjmvPIgmkUAX9l3C0R&_nc_ht=scontent.fscl11-2.fna&oh=00_AfD2nHlmuwRGy6sDf3lV06Ml5-k5EC3IQAsYZM9eW8rulQ&oe=63F4484E)
10.2.![Descripción de la imagen](https://scontent.fscl11-1.fna.fbcdn.net/v/t39.30808-6/331933886_1413855832485841_4473111276968359931_n.jpg?stp=cp6_dst-jpg&_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_ohc=lRVx-Z9cy1MAX9r9Z7m&_nc_ht=scontent.fscl11-1.fna&oh=00_AfBOr8mR14B94H1bBAPhLDpDcHHBQS9REtMPEWugBaU0pQ&oe=63F43866)
10.3.![Descripción de la imagen](https://scontent.fscl11-2.fna.fbcdn.net/v/t39.30808-6/331549010_3758552564371872_5281027802686922001_n.jpg?stp=cp6_dst-jpg&_nc_cat=103&ccb=1-7&_nc_sid=730e14&_nc_ohc=uf9BfrhqNuQAX_AvURF&_nc_ht=scontent.fscl11-2.fna&oh=00_AfBgrZqj-RVqb3GPqiArJDVkylgp_EE9PpKi63YcRDxeig&oe=63F4A86D)
11. Una vez se haya importado el contenido del json a la base de datos podemos ingresar a la ruta http://localhost:8000/testchr/projects en la cual hay una tabla que muestra todos los datos importados o en su defecto revisar los datos en el admin: http://localhost:8000/admin/testchr/project/





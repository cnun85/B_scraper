# B_scraper
Scrapper del buscador de Bing construido con Python 3.8 y el framework Scrapy.

## Instalación y ejecución
Hay dos formas de correr la aplicación. Como proyecto Python o dentro de un docker.

### 1. instalación básica

Instalación de Python 3 (Python 3.8 used in this app)

*Recomendado hacer desde aqui con un entorno virtual.

iniciar entorno virtual:

	$ cd B_escraper-main
	$ py -3 -m venv venv
	$ venv\Scripts\activate

Dependencias:

	$ python -m pip install --upgrade pip
	$ pip3 install -r requirements.txt

#### Ejecutando la aplicación:

	$ python bingScraper.py arg1 arg2 (los argumentos son la lista de términos como "test" o "enthec")
  
 para abandonar el entorno virtual:

	$ deactivate

### 2. Docker (requiere instalación de Docker previa)
*Atención, para correr la aplicación en un docker, se ha de liberar el puerto que vaya a ser usado por el contenedor si estuviera en uso. A efectos de esta guía será el 8888.

Desde la terminal:

	$ cd B_escraper-main
	$ docker build -t proyecto .
	$ docker run -d -p 8888:8888 proyecto:latest
  
  

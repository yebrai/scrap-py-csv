# Scraping, python y Docker

Este proyecto realiza scraping de una página web para extraer datos de productos y guardarlos en un archivo CSV utilizando un contenedor Docker.

## Requisitos

- [Docker](https://www.docker.com/products/docker-desktop) instalado en tu sistema.

## Instrucciones

### Paso 1: Clonar el repositorio

Clona este repositorio en tu máquina local:

```
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### Paso 2: Construir la imagen Docker

Construye la imagen Docker usando el Dockerfile incluido:

```
docker build -t scraping-container .
```

### Paso 3: Ajustar elementos en el archivo .py

Actualiza los elementos en el scrape_to_csv.py al inspeccionar la web sobra la que quieres scrapear, Completa los puntos 1,2 y 3 del archivo.

### Paso 4: 

Ejecuta el contenedor Docker y monta el volumen para que el archivo CSV se guarde en tu máquina local:

```
docker run -v ${PWD}:/app scraping-container
```

Ahora en el directorio root del proyecto, tienes deberia de haberse creado un archivo con nombre datos_extraidos.csv 
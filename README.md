# Pasos para ejecutar el proyecto

### Crear un entorno virtual

	python -m venv .env

### Ejecutar el entorno

Comando Linux:

	source .env/bin/active

Comando Windows

	.env/Scripts/active

**Para detener el entorno virual ejecutar en la linea de comandos**

	deactivate

## Ejecutar 

	pip install -r requierments.txt

##  Ejecutar enforma consecutiva

	python -m spacy download es_core_news_sm

	python -m spacy download es_core_news_md

## Para usar el servicio ejecutar

	python api.py 

### Rutas del api

	- GET http://localhost:4000/spacy/

Enviar una peticion http GET enviando en el body un objeto Json
``` json
{
  "texto" : "Transcripcion de la historia clinica"
}
``` 
El api retornara un objeto json con los datos del paciente extraidos

----------------
Esta version fue echa en python 3.10.5
La version del modulo spacy utilizada es la 3.4.1

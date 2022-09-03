### Crear un entorno virtual

	python -m venv .env

### Ejecutar el entorno

Comando Linux:

	source .env/bin/active

Comando Windows

	.env/Scripts/active

- Para detener el entorno virual ejecutar en la linea de comandos
		deactivate

## Ejecutar 

	pip install -r requierments.txt

##  Ejecutar enforma consecutiva

	python -m spacy download es_core_news_sm

	python -m spacy download es_core_news_md

## Para usar el servicio ejecutar

	python servicioNlp.py

*Por defecto utiliza el archivo datos6.txt de la carpeta textos*
----------------
Esta version fue echa en python 3.10.5
La version del modulo spacy utilizada es la 3.4.1

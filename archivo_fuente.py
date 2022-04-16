import requests
import os
from datetime import date


hoy = date.today()
folder = hoy.strftime('%Y-%B')
d = hoy.strftime('%d-%m-%Y')
path = os.getcwd()

def descarga_museo():
    
    museo_file = requests.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv', stream=True).content
    directorio = crear_carpeta('museos',folder)
    nombre = f'museos-{d}'
    
    return museo_file, directorio, nombre

def descarga_cine():
    
    cine_file = requests.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv', stream=True).content
    directorio = crear_carpeta('salas_de_cine',folder)
    nombre = f'salas_de_cine-{d}'
    
    return cine_file, directorio, nombre

def descarga_biblio():
    
    biblio_file = requests.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv', stream=True).content
    directorio = crear_carpeta('bibliotecas_populares',folder)
    nombre = f'bibliotecas_populares-{d}'
    
    return biblio_file, directorio, nombre

    
def crear_carpeta(carpeta1,carpeta2):
    try:
        os.mkdir(os.path.join(path, carpeta1, carpeta2))
    except FileExistsError:
        pass
    except FileNotFoundError:
        os.mkdir(os.path.join(path, carpeta1))
        os.mkdir(os.path.join(path, carpeta1,carpeta2))
    
    return os.path.join(path,carpeta1,carpeta2)

def guardar(archivo,directorio,nombre):
    open(os.path.join(directorio,nombre), 'wb').write(archivo)

guardar(descarga_museo()[0],descarga_museo()[1],descarga_museo()[2])
guardar(descarga_cine()[0],descarga_cine()[1],descarga_cine()[2])
guardar(descarga_biblio()[0],descarga_biblio()[1],descarga_biblio()[2])
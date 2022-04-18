import pandas as pd
import os
from datetime import date


hoy = date.today()
folder = hoy.strftime('%Y-%B')
d = hoy.strftime('%d-%m-%Y')
path = os.getcwd()

def buscar(tipo):

    archivo = os.path.join(path,tipo,folder,f'{tipo}-{d}.csv')
    df = pd.read_csv(archivo)

    return df


archivo = buscar('museos')
columns = [0,1,2,4,6,8,9,10,12,14,15,16]
archivo = archivo.iloc[:,columns]
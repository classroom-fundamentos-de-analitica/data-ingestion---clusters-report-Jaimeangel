"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    #
    # Inserte su código aquí
    #
    with open('clusters_report.txt','r') as reporte:
        reporte_lines = reporte.readlines()

    row_completed = []
    row_for_specific_cluster = []

    for row in reporte_lines[4:]:
        #row starting with numbers
        if re.match('^ +\d+ +', row):
            lista = row.split()
            row_for_specific_cluster.append(int(lista[0]))
            row_for_specific_cluster.append(int(lista[1]))
            row_for_specific_cluster.append(float(lista[2].replace(',','.')))
            row_for_specific_cluster.append(' '.join(lista[4:]))
        #row starting with empty spaces and after a word
        elif re.match('^ +\w', row):
            palabras = row.split()
            palabras = ' '.join(palabras)
            row_for_specific_cluster[3] += ' ' + palabras
        #completely empty row
        elif re.match('^\n', row) or re.match('^ +$', row):
            row_for_specific_cluster[3] = row_for_specific_cluster[3].replace('.', '')
            row_completed.append(row_for_specific_cluster)
            row_for_specific_cluster = []

    dataFrame = pd.DataFrame (row_completed, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return dataFrame
ingest_data()
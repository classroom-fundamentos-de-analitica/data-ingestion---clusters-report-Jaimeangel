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

def funcion3():
    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()

    # Expresión regular para encontrar palabras sin números y teniendo en cuenta los guiones entre letras
    pattern = re.compile(r'(\b(?:[a-zA-Z]+(?:-[a-zA-Z]+)?)\b)(?![^\(]*\))')

    modified_lines = []
    for line in lines:
        modified_line = pattern.sub(r'\1, ', line)
        modified_lines.append(modified_line)

    for line in modified_lines:
        print(line)
funcion3()

import pandas as pd

def ingest_data():
    # Leer las dos primeras líneas del archivo
    with open("clusters_report.txt", "r") as file:
        lines = file.readlines()[:2]

    # Procesar las dos primeras líneas
    processed_lines = []
    for line in lines:
        processed_line = ""
        for i, char in enumerate(line):
            if char.isalpha() and i < len(line) - 1 and line[i+1].isalpha():
                processed_line += char + "_"
            else:
                processed_line += char
        processed_lines.append(processed_line.lower())
    

    # Crear un DataFrame de Pandas
    df = pd.DataFrame(processed_lines)

    # Mostrar el DataFrame
    print(df)
    
ingest_data()

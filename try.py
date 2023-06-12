import pandas as pd
import re

def dataPrint():
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

    df_1 = pd.DataFrame(processed_lines)
    print(df_1)
    

    with open('clusters_report.txt', 'r') as file:
        palabras_clave = file.readlines()[2:]

    # Expresión regular para encontrar palabras sin números y teniendo en cuenta los guiones entre letras
    pattern = re.compile(r'(\b(?:[a-zA-Z]+(?:-[a-zA-Z]+)?)\b)(?![^\(]*\))')

    modified_lines = []
    for line in palabras_clave:
        modified_line = pattern.sub(r'\1, ', line)
        modified_lines.append(modified_line)
    
    df = pd.DataFrame(modified_lines)
    print(df)
dataPrint()   
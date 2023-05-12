import csv

from collections import Counter

import pandas as pd

#Aquí vamos a guardar los pedimentos que encontramos entre las dos búsquedas unidas
pedimentos_totales = set()

# Carga el archivo Excel REPORTE
df = pd.read_excel('table_12.xlsx')

# Extrae la columna "Número Pedimento" y conserva solo el último número
df['Número Pedimento'] = df['Número Pedimento'].astype(str).str.split().str[-1]

# Guarda la columna en un archivo CSV
df['Número Pedimento'].to_csv('table_reporte.csv', index=False)



# Lee el archivo CSV
df = pd.read_csv('table_12.csv')

# Extrae la columna 'Número Pedimento' y conviértela a números con ceros a la izquierda
num_pedimentos = df['Número Pedimento'].astype(str).str.zfill(7)

# Crea un nuevo DataFrame con la columna extraída y convertida
nuevo_df = pd.DataFrame({'Número Pedimento': num_pedimentos})

# Guarda el nuevo DataFrame en un archivo CSV
nuevo_df.to_csv('table_Alex.csv', index=False)

def leer_csv(nombre_archivo):
    valores = []
    with open(nombre_archivo, 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for fila in lector:
            valores.append(fila)
    return valores

# Ejemplo de uso
archivo1 = 'table_reporte.csv'
valores1 = leer_csv(archivo1)
archivo2 = 'table_Alex.csv'
valores2 = leer_csv(archivo2)

def comparar_listas(lista1, lista2):
    # Obtener recuentos de cada elemento en ambas listas
    recuentos1 = Counter(tuple(x) for x in lista1)
    recuentos2 = Counter(tuple(x) for x in lista2)

    # Encontrar los valores que difieren y la cantidad de veces que difieren
    diferencias = {}
    for valor, recuento in recuentos1.items():
        recuento2 = recuentos2.get(valor, 0)
        if recuento != recuento2:
            diferencias[valor] = abs(recuento - recuento2)

    # Imprimir los valores que difieren y la cantidad de veces que difieren
    for valor, diferencia in diferencias.items():
        pedimentos_totales.add(valor[0])
        print(f"El valor {valor[0]} difiere {diferencia} veces")

    nombre_archivo = "test.csv"

    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        for valor, diferencia in diferencias.items():
            escritor.writerow([valor[0], diferencia])


def comparar_listas2(lista1, lista2, nombre_archivo):
    # Obtener conjuntos de números de pedimento en ambas listas
    pedimentos1 = set([item[0] for item in lista1])
    pedimentos2 = set([item[0] for item in lista2])

    # Encontrar los números de pedimento que existen en una lista pero no en la otra
    diferencias = pedimentos1.symmetric_difference(pedimentos2)

    # Guardar los números de pedimento que difieren en un archivo CSV
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        for pedimento in diferencias:
            pedimentos_totales.add(pedimento)
            escritor.writerow([pedimento])




comparar_listas(valores1, valores2)
comparar_listas2(valores1, valores2, 'diferencias.csv')

nombre_archivo = 'pedimentos_totales.csv'

# Guardar los números de pedimento que difieren en un archivo CSV
with open(nombre_archivo, 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)

    for pedimento in pedimentos_totales:
        escritor.writerow([pedimento])

# Archivo de texto con los números de pedimento rectificados
archivo_txt = 'excluidos_rectificados.txt'

# Leer el archivo de texto
with open(archivo_txt, 'r') as archivo:
    contenido = archivo.read()

# Extraer los pedimentos del contenido del archivo de texto
pedimentos_txt = contenido.strip('()\n').split(',')

pedimentos_txt = [valor[4:11] for valor in pedimentos_txt]



rectificados='pedimentos_encontrados_no_rectificados.csv'

# Guardar los números de pedimento que difieren en un archivo CSV
with open(rectificados, 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)

    # Comprobar si los pedimentos encontrados previamente están en el archivo de texto
    for pedimento in pedimentos_totales:
        if pedimento in pedimentos_txt:
            a=2
            #print(f"El pedimento {pedimento} se encuentra en el archivo de texto.")
        else:
            escritor.writerow([pedimento])
            print(f"El pedimento {pedimento} no se encuentra en el archivo de texto.")


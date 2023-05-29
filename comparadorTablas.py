import csv

from collections import Counter

import pandas as pd

#Aquí vamos a guardar los pedimentos que encontramos entre las dos búsquedas unidas
pedimentos_totales = set()

# Carga el archivo Excel REPORTE
df = pd.read_excel('table_reporte.xlsx')

# Extrae las columnas "Sección Aduanal", "Patente" y "Número Pedimento"
df_extracted = df[['Sección Aduanera', 'Patente', 'Número Pedimento']]
# Extrae la columna "Número Pedimento" y conserva solo el último número
df_extracted['Número Pedimento'] = df_extracted['Número Pedimento'].astype(str).str.split().str[-1]
df_extracted['Sección Aduanera'] = df['Sección Aduanera'].astype(str).str.zfill(3)
# Guarda las columnas en un archivo CSV
df_extracted.to_csv('table_reporte.csv', index=False)

# Combinar los campos en una sola columna
fusion = df_extracted.apply(lambda x: ' '.join(x.astype(str)), axis=1)

# Guardar los campos fusionados en un archivo CSV
fusion.to_csv('total.csv', index=False)



# Lee el archivo CSV
df = pd.read_csv('181.csv')

# Extrae la columna 'Número Pedimento' y conviértela a números con ceros a la izquierda
num_pedimentos = df['Número Pedimento'].astype(str).str.zfill(7)

# Extrae las columnas "Sección Aduanal", "Patente" y "Número Pedimento"
df_extracted = df[['Sección Aduanera', 'Patente', 'Número Pedimento']]
# Extrae la columna "Número Pedimento" y conserva solo el último número
df_extracted['Número Pedimento'] = df_extracted['Número Pedimento'].astype(str).str.zfill(7)
df_extracted['Patente'] = df_extracted['Patente'].astype(str).str.zfill(4)
df_extracted['Sección Aduanera'] = df_extracted['Sección Aduanera'].astype(str).str.zfill(3)

#Guardemos las columnas en el csv
df_extracted.to_csv('table_Alex.csv', index=False)

fusion = df_extracted.apply(lambda x: ' '.join(x.astype(str)), axis=1)

# Guardar los campos fusionados en un archivo CSV
fusion.to_csv('total_second.csv', index=False)

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
    contador_total = 0
    # Imprimir los valores que difieren y la cantidad de veces que difieren
    for valor, diferencia in diferencias.items():
        pedimentos_totales.add(valor[0])
        print(f"El valor {valor[0]} difiere {diferencia} veces")
        contador_total = contador_total + diferencia
    print( f"recuento total es {contador_total}"  )
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
patente_txt = [valor[0:4] for valor in pedimentos_txt]
seccion_aduanera_txt = [valor[11:14] for valor in pedimentos_txt]
pedimentos_txt = [valor[4:11] for valor in pedimentos_txt]




rectificados='pedimentos_encontrados_no_rectificados.csv'

# Guardar los números de pedimento que difieren en un archivo CSV
with open(rectificados, 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)

    # Comprobar si los pedimentos encontrados previamente están en el archivo de texto
    for pedimento in pedimentos_totales:
        if pedimento in pedimentos_txt or pedimento in patente_txt or pedimento in seccion_aduanera_txt:
            a=2
            #print(f"El pedimento {pedimento} se encuentra en el archivo de texto.")
        else:
            escritor.writerow([pedimento])
            print(f"El pedimento {pedimento} no se encuentra en el archivo de texto.")


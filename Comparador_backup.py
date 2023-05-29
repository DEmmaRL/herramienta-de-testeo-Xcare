import csv

from collections import Counter

import pandas as pd

#Aquí vamos a guardar los pedimentos que encontramos entre las dos búsquedas unidas
pedimentos_totales = set()

ruta_archivo = r'C:\Users\demma\Downloads\Reporte_entregable_de_Auditoria CONTINENTAL 2021.xlsm'
nombre_hoja = '3.1'
numero_fila_encabezado = 1  # Número de fila del encabezado

df = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, header=numero_fila_encabezado)
print(df.columns)
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
df = pd.read_csv(r'C:\Users\demma\Downloads\Resultados Reporte Actualizado 08052023 (1)\3-1_DETALLE DE CONTRIBUCIONES A NIVEL PARTIDA.csv')
print(df.columns)

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
comparar_listas2(valores1, valores2, 'diferencias_directo.csv')

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


def Concatenar_datos(archivo_entrada , archivo_salida) :
    # Abrir el archivo de entrada y crear el archivo de salida
    with open(archivo_entrada, 'r') as file_in, open(archivo_salida, 'w', newline='') as file_out:
        reader = csv.reader(file_in, delimiter=' ')
        writer = csv.writer(file_out)

        filas = []  # Lista para almacenar las filas del archivo de entrada

        for row in reader:
            filas.append(row)  # Almacenar cada fila en la lista

        # Reorganizar el orden de las filas
        filas_ordenadas = filas[1:] + [filas[0]]

        for fila in filas_ordenadas:
            fila_sin_espacios = ''.join(fila)
            writer.writerow([fila_sin_espacios])

    print("Se han eliminado todos los espacios en blanco y se ha guardado en el archivo 'datos_salida.csv'.")

archivo_entrada = 'total.csv'
archivo_salida = 'z_xcare.csv'
Concatenar_datos(archivo_entrada , archivo_salida)
archivo_entrada = 'total_second.csv'
archivo_salida = 'z_origin.csv'
Concatenar_datos(archivo_entrada , archivo_salida)



# Rutas de los archivos CSV
archivo1 = 'z_xcare.csv'
archivo2 = 'z_origin.csv'

archivo_exclusion = 'excluidos_rectificados.txt'

archivo_salida = 'salida.txt'

archivo_diferencias = 'diferencias.txt'

# Diccionarios para almacenar los recuentos de cada número en cada archivo
recuentos1 = {}
recuentos2 = {}

# Leer archivo de exclusión y crear un conjunto con los números a excluir
numeros_exclusion = set()
with open(archivo_exclusion, 'r') as file_exclusion:
    numeros_exclusion.update(linea.strip() for linea in file_exclusion.read().split(','))

# Leer archivo1 y contar las ocurrencias de cada número (excluyendo los números de exclusión)
with open(archivo1, 'r') as file1:
    reader1 = csv.reader(file1)
    for row in reader1:
        numero = row[0]
        if numero not in numeros_exclusion:
            if numero in recuentos1:
                recuentos1[numero] += 1
            else:
                recuentos1[numero] = 1

# Leer archivo2 y contar las ocurrencias de cada número (excluyendo los números de exclusión)
with open(archivo2, 'r') as file2:
    reader2 = csv.reader(file2)
    for row in reader2:
        numero = row[0]
        if numero not in numeros_exclusion:
            if numero in recuentos2:
                recuentos2[numero] += 1
            else:
                recuentos2[numero] = 1

# Encontrar los números con recuentos diferentes
numeros_diferentes = set(recuentos1.keys()).symmetric_difference(set(recuentos2.keys()))

# Filtrar los números que están en el archivo de exclusión
numeros_diferentes = [numero for numero in numeros_diferentes if numero not in numeros_exclusion]

# Guardar los números con recuentos diferentes en el archivo de salida
with open(archivo_salida, 'w') as file_salida:
    for numero in numeros_diferentes:
        recuento1 = recuentos1.get(numero, 0)
        recuento2 = recuentos2.get(numero, 0)
        linea = f"Número: {numero}\nRecuento en archivo1: {recuento1}\nRecuento en archivo2: {recuento2}\n---\n"
        file_salida.write(linea)

# Guardar los recuentos de diferencias en un archivo separado
with open(archivo_diferencias, 'w') as file_diferencias:
    for numero, recuento in recuentos2.items():
        if numero not in recuentos1 and numero not in numeros_exclusion or recuentos1[numero] < recuento and numero not in numeros_exclusion:
            recuento1_actual = recuentos1.get(numero, 0)
            if recuento1_actual < recuento :
                linea = f"Número: {numero}\nRecuento en Reporte: {recuento}\nRecuento en X care: {recuento1_actual}\n---\n"
                file_diferencias.write(linea)

print(f"Los resultados se han guardado en el archivo '{archivo_salida}'.")
print(f"Las diferencias se han guardado en el archivo '{archivo_diferencias}'.")
nombre_archivo = "numeros_exclusion.csv"

# Abre el archivo CSV en modo escritura
with open(nombre_archivo, 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)

    # Escribe cada elemento de la lista como una fila en el archivo CSV
    for numero in numeros_exclusion:
        writer.writerow([numero])

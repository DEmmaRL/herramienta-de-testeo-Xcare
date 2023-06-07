import pandas as pd
#Este script sirve para comprobar el número de fracciones
# Cargar los tres archivos Excel en DataFrames
ruta_archivo = r'C:\Users\demma\Downloads\Reporte_entregable_de_Auditoria CONTINENTAL 2021.xlsm'
nombre_hoja = '50'
numero_fila_encabezado = 1  # Número de fila del encabezado

tabla1 = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, header=numero_fila_encabezado)
tabla2 = pd.read_csv('50.csv')
tabla3 = pd.read_excel('50.xlsx')
print(tabla3.columns)
# Contar la frecuencia de cada registro en la columna "Fracción" de tabla1
conteo_tabla1 = tabla1['Fracción'].value_counts().reset_index()
conteo_tabla1.columns = ['Fracción', 'conteo']

# Comparar el conteo de la tabla1 con la cantidad de ocurrencias en la tabla2
errores = []
for index, row in conteo_tabla1.iterrows():
    fraccion = row['Fracción']
    conteo_tabla2 = tabla2['Fracción'].value_counts().get(fraccion, 0)
    if row['conteo'] > conteo_tabla2:
        errores.extend([fraccion] * (row['conteo'] - conteo_tabla2))

# Comprobar si los errores se encuentran en la columna "Fracción" de tabla3
fracciones_no_encontradas = []
for fraccion in errores:
    if fraccion in tabla3['FRACCIÓN'].values:
        print(fraccion)  # Imprimir en la terminal
        fracciones_no_encontradas.append(fraccion)

# Guardar las fracciones no encontradas en un archivo de texto
with open('fracciones_no_encontradas.txt', 'w') as file:
    for fraccion in fracciones_no_encontradas:
        if fraccion in tabla3['FRACCIÓN']:
            file.write(str(fraccion) + '\n')

import pandas as pd

# Cargar el archivo CSV
df_csv = pd.read_csv('table_61.csv')
df_extracted_csv = df_csv[['Sección Aduanera', 'Patente', 'Número Pedimento']]
# Cargar el archivo Excel
df_excel = pd.read_excel('table_reporte.xlsx')
df_extracted_excel = df_excel[['Sección Aduanera', 'Patente', 'Número Pedimento']]
# Combinar los datos en un solo DataFrame
df_combined = pd.concat([df_extracted_csv, df_extracted_excel])

# Encontrar los registros duplicados
duplicados = df_combined[df_combined.duplicated(keep=False)]

# Imprimir las filas duplicadas
if not duplicados.empty:
    for indice, fila in duplicados.iterrows():
        print(f"Fila {indice}: {fila}")

# Imprimir el número total de filas duplicadas
num_duplicados = len(duplicados)
print(f"Número total de filas duplicadas: {num_duplicados}")

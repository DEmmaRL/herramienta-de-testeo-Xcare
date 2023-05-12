import pandas as pd

# Lee el archivo CSV
df = pd.read_excel('tabla_reporte.xlsm')

# Extrae la columna 'Número Pedimento' y conviértela a números con ceros a la izquierda
num_pedimentos = df['Número Pedimento'].astype(str).str.zfill(7)

# Crea un nuevo DataFrame con la columna extraída y convertida
nuevo_df = pd.DataFrame({'Número Pedimento': num_pedimentos})

# Guarda el nuevo DataFrame en un archivo CSV
nuevo_df.to_csv('table_reporte.csv', index=False)

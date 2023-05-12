import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('table_13.csv')

# Extrae la columna 'Número Pedimento' y conviértela a números con ceros a la izquierda
num_pedimentos = df['Numero Pedimento'].astype(str).str.zfill(7)

# Crea un nuevo DataFrame con la columna extraída y convertida
nuevo_df = pd.DataFrame({'Numero Pedimento': num_pedimentos})

# Guarda el nuevo DataFrame en un archivo CSV
nuevo_df.to_csv('table_Alex.csv', index=False)

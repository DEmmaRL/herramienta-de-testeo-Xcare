import pandas as pd

# Carga el archivo Excel
df = pd.read_excel('tabla_reporte.xlsm')

# Extrae la columna "Número Pedimento" y conserva solo el último número
df['Número Pedimento'] = df['Número Pedimento'].astype(str).str.split().str[-1]

# Guarda la columna en un archivo CSV
df['Número Pedimento'].to_csv('table_reporte.csv', index=False)

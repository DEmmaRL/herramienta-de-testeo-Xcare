import csv

from collections import Counter

import pandas as pd


columns_to_read = ['RFC', 'Sección Aduanera', 'Patente']
dfe = pd.read_csv('181.csv', usecols=columns_to_read)
dfe.to_csv('testeo.csv', index=False)

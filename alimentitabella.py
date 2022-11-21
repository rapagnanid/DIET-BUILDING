# Import libraries
import re
import pandas as pd
from tabula import read_pdf

# Read the PDF file and convert into a DataFrame
tables = read_pdf("alimenti-tabella.pdf", pages="all", multiple_tables=False, lattice=True)
df = pd.DataFrame(tables[0])
#print(df)

# Clean the DataFrame
df.rename(columns = {'Alimenti':'Alimenti',
                     'kcal':'KCal',
                     '% parte\redule':'% parte edule',
                     'Proteine\r(g)':'Proteine (g)',
                     'Lipidi (g)':'Lipidi (g)',
                     'Glucidi\rdisponibili\r(g)':'Carboidrati (g)',
                     'Amido\r(g)':'Amido (g)'
                     }, inplace = True)

df = df.dropna().reset_index(drop=True)

del df['% parte edule']
del df['Amido (g)']

df['Proteine (g)'] = df['Proteine (g)'].astype('string')
df['Lipidi (g)'] = df['Lipidi (g)'].astype('string')
df['Carboidrati (g)'] = df['Carboidrati (g)'].astype('string')

df['Proteine (g)'] = df['Proteine (g)'].str.replace(',', '.')
df['Lipidi (g)'] = df['Lipidi (g)'].str.replace(',', '.')
df['Carboidrati (g)'] = df['Carboidrati (g)'].str.replace(',', '.')

df['Proteine (g)'] = df['Proteine (g)'].astype('float')
df['Lipidi (g)'] = df['Lipidi (g)'].astype('float')
df['Carboidrati (g)'] = df['Carboidrati (g)'].astype('float')

df_def = df
df_def_calorie = df_def[['Alimenti', 'KCal']]
df_def_carboidrati = df_def[['Alimenti', 'Carboidrati (g)']]
df_def_proteine = df_def[['Alimenti', 'Proteine (g)']]
df_def_lipidi = df_def[['Alimenti', 'Lipidi (g)']]

"""
print(df['KCal'].dtypes)
print(df['Proteine (g)'].dtypes)
print(df['Lipidi (g)'].dtypes)
print(df['Carboidrati (g)'].dtypes)
print(df.head(5))
"""
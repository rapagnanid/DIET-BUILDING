# Import libraries
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
print(df.head(5))

print(df.describe())
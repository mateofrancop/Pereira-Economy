# Se cargan los datos limpiados previamente a mysql

import pandas as pd
from sqlalchemy import create_engine

db = 'pereira'
table = 'all_data'

url = 'mysql+mysqlconnector://root:1004519044@localhost/'

engine = create_engine(url + db, echo = False)


# Se Carga el archivo XLSX en un DataFrame
df = pd.read_excel(r'C:\Users\Alvaro\OneDrive\Documentos\Primer proyecto\codigo\Economia_Pereira\Data\Datos_Pereira_info.xlsx')

print('real ok')

df.to_sql(name = table, con = engine, if_exists = 'append', index = False)

    
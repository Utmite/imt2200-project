import pandas as pd

# URL de la página de Wikipedia
url = 'https://es.wikipedia.org/wiki/Anexo:Comunas_de_Chile'

# Leer las tablas de la página
tablas = pd.read_html(url)

# Seleccionar la primera tabla
primera_tabla = tablas[0]

# Guardar la tabla en un archivo CSV
primera_tabla.to_csv('tabla_wikipedia.csv', index=False)

print('Tabla guardada como "tabla_wikipedia.csv"')

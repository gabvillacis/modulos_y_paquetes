# %%
# pathlib: https://docs.python.org/3/library/pathlib.html

# importando la clase Path desde módulo pathlib
from pathlib import Path

# %%
# definiendo una ruta de directorio
path_directorio = Path("C:\\Program Files\\Microsoft")
print(path_directorio)

# %%
# definiendo ruta al directorio actual
path_directorio_actual = Path()
print(path_directorio_actual)
print(path_directorio_actual.absolute())

# %%
# definiendo ruta relativa hacia un archivo
path_archivo = Path("datasets/googleplaystore.csv")
print(path_archivo)

# %%
# obteniendo el directorio del usuario del sistema operativo
print(Path.home())

# %%
# comprobar si la ruta existe
path = Path("datasets/googleplaystore.csv")
print(path.exists())

# %%
# comprobar si la ruta es un archivo
print(path.is_file())

# %%
# comprobar si la ruta es un directorio
print(path.is_dir())

# %%
# obteniendo el nombre del componente final de la ruta
print(f'Ruta absoluta: {path.absolute()}')
print(f'Componente final: {path.name}')

# %%
# obteniendo el nombre del componente final de la ruta sin el sufijo (extensión)
print(f'Ruta absoluta: {path.absolute()}')
print(f'Componente final sin sufijo: {path.stem}')

# %%
# obteniendo el último sufijo (extensión) del componente final
print(f'Ruta absoluta: {path.absolute()}')
print(f'Sufijo: {path.suffix}')

# %%
# obteniendo el directorio padre donde se encuentra el archivo
print(f'Ruta absoluta: {path.absolute()}')
print(f'Directorio padre: {path.parent}')
print(f'Directorio padre absosulo: {path.parent.absolute()}')

# %%
# reemplazando solo el nombre del archivo dentro de la ruta
print(f'Ruta absoluta: {path.absolute()}')
print(path.with_name("googleplaystore_renombrado.csv"))
# %%

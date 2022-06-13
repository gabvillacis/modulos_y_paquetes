# %%
# importando la clase Path desde módulo pathlib
from pathlib import Path

# %%
# verificando existencia de directorio
path = Path('D:\\directorio_pruebas')
print(path.absolute())
print(path.exists())

# %%
# creando y borrando directorio
if(not path.exists()):
    path.mkdir()
else:
    path.rmdir()
    path.mkdir()

# %%
# renombrando directorio
path_renombrado = path.rename("D:\\directorio_pruebas_renombrado")
print(path_renombrado.absolute())

# %%
# apuntando al directorio actual
directorio_actual = Path()
print(directorio_actual)
print(directorio_actual.absolute())

# %%
# listando el contenido del directorio
for p in directorio_actual.iterdir():
    print(p)

# %%
# obteniendo el contenido del directorio como una lista
paths = [p for p in directorio_actual.iterdir()]
print(paths)

# %%
# obteniendo solo los subdirectorios
paths = [p for p in directorio_actual.iterdir() if p.is_dir()]
print(paths)

# %%
# obteniendo solo los archivos python
archivos_python = [p for p in directorio_actual.glob("*.py")]
print(archivos_python)

# %%
# obteniendo solo los archivos python de forma recursiva
archivos_python = [p for p in directorio_actual.rglob("*.py")]
print(archivos_python)
# %%

# importando la clase Path desde módulo pathlib
from pathlib import Path

path = Path("D:\\carpeta_pruebas")

print(path.exists())

if(not path.exists()):
    path.mkdir()
else:
    path.rmdir()
    path.mkdir()

print(path.absolute())
# nuevo_path = path.rename("D:\\carpeta_pruebas_renombrado")
# print(nuevo_path.absolute())

directorio_actual = Path()

# listando el contenido del directorio
for p in directorio_actual.iterdir():
    print(p)

# obteniendo el contenido del directorio como una lista
paths = [p for p in directorio_actual.iterdir()]
print(paths)

paths = [p for p in directorio_actual.iterdir() if p.is_dir()]
print(paths)

archivos_python = [p for p in directorio_actual.glob("*.py")]
print(archivos_python)

archivos_python = [p for p in directorio_actual.rglob("*.py")]
print(archivos_python)
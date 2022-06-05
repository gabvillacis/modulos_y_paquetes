# pathlib: https://docs.python.org/3/library/pathlib.html

# importando la clase Path desde módulo pathlib
from pathlib import Path

# trabajando con rutas
path1 = Path("C:\\Program Files\\Microsoft")
print(path1)

path_carpeta_actual = Path()
print(path_carpeta_actual)

path_archivo = Path("datasets") / Path("googleplaystore.csv")
print(path_archivo)

path_archivo = Path("datasets\\googleplaystore.csv")
print(path_archivo)

# obteniendo el directorio del usuario del sistema operativo
print(Path.home())

path = Path("datasets/googleplaystore.csv")
# comprobar si la ruta existe
print(path.exists())

# comprobar si la ruta es un archivo
print(path.is_file())

# comprobar si la ruta es un directorio
print(path.is_dir())

# obteniendo el nombre del componente final de la ruta
print(path.name)

# obteniendo el nombre del componente final de la ruta sin el sufijo (extensión)
print(path.stem)

# obteniendo el último sufijo (extensión) del componente final
print(path.suffix)

# obteniendo el directorio padre donde se encuentra el archivo
print(path.parent)

# obteniendo la ruta absoluta
print(path.absolute())

print(path)

# reemplazando solo el nombre del archivo dentro de la ruta
print(path.with_name("archivo.txt"))
# importando la clase Path desde módulo pathlib
from pathlib import Path
from datetime import datetime

path = Path("datasets/words.txt")

# comprobar si existe el archivo
path.exists()

# obtener los metadatos del archivo
result = path.stat()
print(result)
print(f"Tamaño: {result.st_size} bytes")
print(f"Tamaño: {result.st_size / 1024} KB")
print(f"Tamaño: {result.st_size / 1024 / 1024} MB")

print(f"Fecha Creación: {datetime.fromtimestamp(result.st_ctime)}")
print(f"Fecha Modificación: {datetime.fromtimestamp(result.st_atime)}")

# creando un nuevo archivo
file_path = Path("datasets/words.txt")
with file_path.open("w", encoding="utf-8") as f:
    for i in range(50):
        f.write(f"linea {i+1} del archivo\n")

# añadiendo contenido al archivo
with file_path.open("a", encoding="utf-8") as f:
    lineas = [f"linea adicional {i+1}\n" for i in range(100)]
    f.writelines(lineas)
    f.write("linea extra 1\n")
    f.write("linea extra 2\n")

# añadiendo y leyendo el contenido del archivo
with file_path.open("a+", encoding="utf-8") as f:
    f.write("linea nueva agregada\n")

    for linea in f.readlines():
        print(linea)

# otros modos de apertura de archivos: https://www.tutorialspoint.com/python/python_files_io.htm
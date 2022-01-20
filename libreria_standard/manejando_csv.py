# csv: https://docs.python.org/3/library/csv.html

import csv

# leyendo archivo csv
with open("datasets/googleplaystore.csv", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for linea_csv in csv_reader:
        print(linea_csv)

# leyendo archivo csv en un diccionario
with open("datasets/googleplaystore.csv", encoding='utf-8') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file, delimiter=',')
    for dict_entry in csv_dict_reader:
        print(dict_entry)

# escribiendo archivo csv mediante la función writerow
with open("datasets/estudiantes.csv", encoding='utf-8', mode='w+') as csv_file:
    writer = csv.writer(csv_file, delimiter = ',', lineterminator='\n')

    writer.writerow(["Gabriel", "Villacis", 28, "Guayaquil"])
    writer.writerow(["Marta", "Gonzales", 25, "Ambato"])
    writer.writerow(["Hugo", "Torres", 20, "Quito"])
    writer.writerow(["Marcos", "Benavides", 18, "Quito"])

# escribiendo archivo csv mediante un diccionario
with open("datasets/estudiantes.csv", encoding='utf-8', mode='w+') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['nombre', 'apellido', 'edad', 'ciudad'], lineterminator='\n')

    lista_estudiantes = [   {'nombre': 'Jose', 'apellido': 'Lopez', 'edad': 50 },
                            {'nombre': 'Andrea', 'apellido': 'Rodriguez', 'edad': 45 },
                            {'nombre': 'Carlos', 'apellido': 'Jimenez', 'edad': 18}]

    writer.writeheader()
    writer.writerows(lista_estudiantes)
    writer.writerow({'nombre': 'Juan Carlos', 'edad': 22})







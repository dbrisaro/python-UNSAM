"""
Ejercicio 2.5 - Lectura de archivos de datos

Dani Risaro
"""

def costo_camion(nombre_archivo):

    costo = 0

    f = open(nombre_archivo, 'rt')
    headers = next(f).split(',')

    for line in f:
        lista = line.split(',')
        cantidad_cajones = int(lista[1])
        precio_cajon = float(lista[2])
        costo = costo + cantidad_cajones*precio_cajon

    f.close()

    return costo

nombre = 'Data/camion.csv'

costo = costo_camion(nombre)

print(f'Costo total {costo:0.2f}')

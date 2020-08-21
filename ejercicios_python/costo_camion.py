"""
Ejercicio 2.2 - Lectura de archivos de datos

Dani Risaro
"""
costo = 0

f = open('Data/camion.csv', 'rt')
headers = next(f).split(',')

for line in f:
    lista = line.split(',')
    cantidad_cajones = int(lista[1])
    precio_cajon = float(lista[2])
    costo = costo + cantidad_cajones*precio_cajon

print(f'Costo total {costo:0.2f}')

f.close()

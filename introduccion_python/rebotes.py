"""
Ejercicio 1.5 - La pelota que rebota

Dani Risaro
"""

# Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que
# toca el piso salta 3/5 de la altura desde la que cayó. Imprimir una tabla
# mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.


h = 100     # altura inicial

for i in range(10):

    h = h*3/5;
    print(i+1, round(h,4))

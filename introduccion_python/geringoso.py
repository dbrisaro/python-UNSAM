"""
Ejercicio 1.18 - Geringoso

Dani Risaro
"""

cadena = 'ferrocarril'
capadepenapa = ''
vocales = 'a,e,i,o,u'

for c in cadena:
    if c in vocales:
        silaba =  'p' + c
        capadepenapa = capadepenapa + c + silaba
    else:
        capadepenapa = capadepenapa + c

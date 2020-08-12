"""
Ejercicio 1.29 - Traductor al lenguaje inclusivo

Dani Risaro
"""
frase = 'Todos, tu también'
palabras = frase.split()
frase_t = []

for palabra in palabras:
    if 'o' in palabra[-2::]:
        rep = palabra[-2::].replace('o','e',2)
        palabra = palabra[:-2] + rep
    frase_t.append(palabra)

frase_t = ' '.join(frase_t)
print(frase_t)

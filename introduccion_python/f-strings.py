"""
Ejercicio 1.20 - La hipoteca de David con f-string

Dani Risaro
"""

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print(f'Total pagado ${total_pagado:0.2f}')

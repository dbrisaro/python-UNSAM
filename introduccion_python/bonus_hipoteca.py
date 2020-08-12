"""
Ejercicio 1.11 - Bonus hipoteca

Dani Risaro
"""

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if mes >= pago_extra_mes_comienzo-1 and mes < pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    if saldo < 0:
        pago_mensual = pago_mensual-saldo
        saldo = 0
    print(mes, round(total_pagado,2), round(saldo,2))

print('Total pagado:', round(total_pagado, 1))
print('Meses:', mes)

import pandas as pd
import numpy_financial as npf

#Calculando una tabla de amortización de un préstamo

import tabulate as tab
def makeAmortTable(capital, tasa, plazo):        
    
    cuota = round(npf.pmt(tasa, plazo, -capital, 0), 0)
    datos = []
    saldo = capital

    for i in range(1, plazo+1):
        pago_capital = npf.ppmt(tasa, i, plazo, -capital, 0)
        pago_int = cuota - pago_capital
        saldo -= pago_capital  
        linea = [i, format(cuota, '0,.0f'), format(pago_capital, '0,.0f'), format(pago_int, '0,.0f'), format(saldo, '0,.0f')]
        datos.append(linea)

    return tab.tabulate(datos, headers=['Periodo', 'Cuota', 'Capital', 'Intereses', 'saldo'], tablefmt='psql')

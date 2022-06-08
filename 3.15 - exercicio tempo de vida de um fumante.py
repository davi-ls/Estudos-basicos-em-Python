# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 21:24:09 2022

@author: Davi
"""

qtd_cigarros = int(input("Informe a quantidade de cigarros fumados por dia: "))
qtd_anos_fumando = int(input("Informe a quantidade de anos fumando: "))
qtd_dias_fumando = qtd_anos_fumando * 365
qtd_total = qtd_cigarros * qtd_dias_fumando

minutos_perdidos = qtd_total * 10
print(f'### CALCULANDO ###')
print(f'A pessoa perdeu {minutos_perdidos/60:5.2f} horas de vida')
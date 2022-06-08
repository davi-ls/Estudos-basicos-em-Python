# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 21:14:13 2022

@author: Davi
"""

print("Seja bem-vindo.")
km_perc = float(input("Qual a quantidade de KM percorridos?"))
dias_uso = int(input("Qual a quantidade de dias utilizados?"))

calculo_dias = dias_uso * 60
calculo_km = km_perc * 0.15
total = calculo_dias + calculo_km

print(f"Você utilizou o veículo por {dias_uso} e utilizou um total de {km_perc} percorridos ")
print(f"logo, você deve pagar {total} em reais")
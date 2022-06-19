# -*- coding: utf-8 -*-
# Elaborado como exercício pessoal a partir de exercício próprio 
"""
Created on Sun Jun 19 11:17:28 2022

@author: Davi
"""

valor = float(input("Diga o valor: "))
soma = valor
soma += 1
print(f"Operador += -> {soma:0.0f}")
subtrair =  valor
subtrair -= 1
print(f"Operador -= -> {subtrair:0.0f}")
multiplicar = valor
multiplicar *= 2
print(f"Multiplicar por 2x com operador *= -> {multiplicar:0.0f} ")

dividir = valor
dividir /= 2
print(f"Dividir por 2 com operador /= -> {dividir} ")

#exponenciação
exponenciação = valor
exponenciação **= 2
print(f"Exponenciação por 2 com operador **= -> {exponenciação}")

# ignora os valores depois da vírgula
divInteira = valor
divInteira //= 4

print(f"Parte inteira da divisão por 4 com operador //= -> {divInteira}")

# módulo
modulo = valor
modulo %= 4
print(f"Módulo da divisão por 4 com operador %= -> {modulo}")


# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
maior = 0
menor = 0

if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1
    
if numero3 > maior:
    maior = numero3
    
if numero3 < menor:
    menor = numero3


print(f"O maior número é {maior} e o menor é {menor}")
# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem criados a partir de situações
# criadas no livro acima mencionado

salario = float(input("Informe o salário do funcionário: "))
base = 1250
porc_aumento = 0
if salario <= base:
    porc_aumento = 0.10
    aumento = (salario * porc_aumento) + salario

else:
    porc_aumento = 0.15
    aumento = (salario * porc_aumento) + salario

aumento_perc = porc_aumento * 100
print(f"O salário de R${salario} receberá um aumento e ficará com valor de R${aumento:5.2f} a partir do aumento de {aumento_perc:0.0f}%.")
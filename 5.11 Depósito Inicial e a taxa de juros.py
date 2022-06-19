# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado

print ("welcome!")
depInicial = float(input("Digite o valor do depósito inicial: "))
txJuros = float(input("Digite a taxa de juros da poupança: "))
mes = 0
valorJuros = depInicial

print("************************************************************")
print(f"Valor inicial: {depInicial}")
print(f"Taxa de Juros: {txJuros} % ao mês durante 24 meses")
while mes < 24:
   mes = mes + 1
   if (mes == 1):
       Acumulador = depInicial
       Juros = Acumulador * (txJuros / 100)
       soma = Acumulador + Juros
       print(f"{mes:5.2f}. Juros: R$ {Juros:5.2f} Soma: R$ {soma:5.2f}")
   else: 
       Juros = soma * (txJuros / 100)
       soma = soma + Juros
       print(f"{mes:5.2f}. Juros: R$ {Juros:5.2f} Soma: R$ {soma:5.2f}")
print("************************************************************")

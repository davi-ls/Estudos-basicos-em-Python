# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado

print ("welcome!")
depInicial = float(input("Digite o valor do depósito inicial: "))
txJuros = float(input("Digite a taxa de juros da poupança: "))
depMensal = float(input("Digite o valor do depósito mensal: "))

mes = 0
soma = 0
AcumulaJuros = 0

limitador = depInicial
meses = depInicial / depMensal
jurosMensal = 0
print("************************************************************")
print(f"Valor inicial: {depInicial}")
#print(f"Taxa de Juros: {txJuros} % ao mês durante 24 meses")
while mes < meses:
   mes = mes + 1
   if (mes == 1):
       Acumulador = depInicial
       Juros = Acumulador * (txJuros / 100)
       soma = Acumulador + Juros
       AcumulaJuros = AcumulaJuros + Juros
       #print(f"{mes}. Juros: R$ {Juros:5.2f} Soma: R$ {soma:5.2f}")
   else: 
       Juros = soma * (txJuros / 100)
       soma = soma + Juros
       AcumulaJuros = AcumulaJuros + Juros
       #print(f"{mes}. Juros: R$ {Juros:5.2f} Soma: R$ {soma:5.2f} Acumulado de Juros: {AcumulaJuros:5.2f}")
print("************************************************************")
print(f"Acumulado de juros: R$ {AcumulaJuros:5.2f} em {meses:1.0f} meses")
jurosMensal = AcumulaJuros / meses
print(f"Juros mensal a ser pago: {jurosMensal:5.2f}")
print(f"Parcela: {depMensal + jurosMensal:5.2f}")



         
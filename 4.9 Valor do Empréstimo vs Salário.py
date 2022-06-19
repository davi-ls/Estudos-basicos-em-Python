# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado

valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual é o seu salário? "))
qtdAnos = float(input("Quantidade de anos que deseja pagar? "))

qtdParcMensais = qtdAnos * 12
print (f"qtdParcMensais")
porcSalarioNaParcela = ((valorCasa / qtdParcMensais) * 100) / salario
valorParcela = (valorCasa / qtdParcMensais)
if porcSalarioNaParcela < 30:
    print (f"Meus parabéns, você pode financiar sua casa em {qtdParcMensais} parcelas e o valor da parcela é de {valorParcela:5.2f}")
else: 
    print("Você não pode financiar porque o limite de comprometindo da renda é de até 30%")
    print(f"Pelos valores informados você teria um comprometimento de renda de {porcSalarioNaParcela:5.2f}%, o que ultrapassa os limites.")
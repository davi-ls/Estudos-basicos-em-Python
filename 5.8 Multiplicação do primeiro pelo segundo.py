# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado

print("Multiplicação utulizando apenas + e -")

primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número:  "))  

x=1
calculo = 0
while x <= primeiroNumero:
    calculo = calculo + segundoNumero
    x = x + 1
print (f"O resultado é {calculo:1.0f}" )


print("Fim do programa.")
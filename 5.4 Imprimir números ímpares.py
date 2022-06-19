# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado

fim = int(input("Digite o valor para finalizar a sessão: "))
x = 0
while x <= fim:
    if ( x % 2 != 0):
        print(x)
    x = x + 1
print("Programa encerrado")
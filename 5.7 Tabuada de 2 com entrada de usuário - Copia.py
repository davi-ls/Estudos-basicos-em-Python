# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado

print("Tabuada de 2")
inicio = int(input("Digite o valor de início da tabuada: "))
fim = int(input("Digite o valor de fim da tabuada: "))
x = inicio
tabuada = 2
while x<=fim:
    valor = x * tabuada
    print (f"{tabuada} x {x}: {valor}" )
    x = x + 1
    
print("Fim do programa.")
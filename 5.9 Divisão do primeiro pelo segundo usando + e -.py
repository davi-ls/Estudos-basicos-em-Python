# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado

print("Divisão utilizando apenas + e -")

primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número:  "))  

x = 0
resto = 0
count = 0

while x < primeiroNumero:
     x = x + segundoNumero
     if (x > primeiroNumero):
         x = x - segundoNumero
         resto = primeiroNumero - x
         break
     count = count + 1
      

print("**************************")
print(f"Resposta é {count}")
print(f"Resto é {resto}")
print("**************************")
print("Fim do programa.")




# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado

number1 = float(input("Digite o primeiro numero: "))
number2 = float(input("Digite o segundo numero: "))
print("Escolha um Operador matemático: ")
print("+ para somar ")
print("- para diminuir ")
print("* para multiplicação ")
print("/ para divisão ")

operator = input("Digite: ")
valor = 0


if operator == "+":
    valor = number1 + number2
elif operator == "-":
    valor = number1 - number2
elif operator == "*":
    valor = number1 * number2
elif operator == "/":
    valor = number1 / number2
else: 
    print("Você escolheu uma operação inválida")
   
print(f"Você digitou a operação {operator} e o valor da operação é {valor:5.2f}")
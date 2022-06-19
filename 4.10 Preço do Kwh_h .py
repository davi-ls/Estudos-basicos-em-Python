# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado

kwh = float(input("Informa a quantidade de KW/H consumido?" ))
print ("Tipos de Instalação: ")
print ("R para Residências")
print ("I para Indústrias")
print ("C para Comércios")

TipoInstalacao = input("Digite aqui: ")
preco = 0

if TipoInstalacao == "R":
   if kwh <= 500:
       preco = kwh * 0.40
   else: 
       preco = kwh * 0.65
       
if TipoInstalacao == "C":
   if kwh <= 1000:
       preco = kwh * 0.55
   else: 
       preco = kwh * 0.60
       
if TipoInstalacao == "I":
   if kwh <= 5000:
       preco = kwh * 0.55
   else: 
       preco = kwh * 0.60
       
print(f"Você informou um consumo de {kwh} hw/h")
print (f"O valor total a ser pago é de {preco:5.2f} reais")
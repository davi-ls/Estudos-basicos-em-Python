# Este exemplo esta contido no livro 
# Introdução à Programação com Python - 3ª Edição
# Prof. Nilo Ney Coutinho Menezes

# Programa 4.7 - Categoria x Preço

categoria = int(input("Digite a categoria do produto: "))
preço = 0
if categoria == 1:
        preço = 10

elif categoria == 2:
        preço = 18
elif categoria == 3:
        preço = 23
elif categoria == 4:
        preço = 26
elif categoria == 5:
        preço = 31
else:
     print("Categoria inválida, digite um valor entre 1 e 5!")

     
# Melhora na usabilidade por Davi com if
if (preço > 0):
    print(f"O preço do produto é: R${preço:6.2f}")
            
# Este exemplo esta contido no livro 
# Introdução à Programação com Python - 3ª Edição
# Prof. Nilo Ney Coutinho Menezes

salário = float(input("Digite o salário para cálculo do imposto: "))
base = salário
imposto = 0

if base >3000: 
    imposto = imposto + ((base-300) * 0.35)
    base = 3000

if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
    print(f"Salário: R${salário:6.2f} Imposto a pagar: R$ {imposto: 6.2f}")
preco_mercadoria = int(input("Qual o preço da mercadoria: "))
desconto_mercadoria = int(input("Qual o desconto da mercadoria em %"))/100

valor_produto = preco_mercadoria - (preco_mercadoria*desconto_mercadoria)

print (f"Valor do produto: {preco_mercadoria}")
print (f"Valor do produto com desconto: {valor_produto}")

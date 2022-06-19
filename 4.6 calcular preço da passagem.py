# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem, criados a partir de situações
# preparadas em exercício no livro acima mencionado

distancia = float(input("Qual a distância a ser percorrida? "))

valorAte200 = 0.50
valorAcima200 = 0.45
passagem = 0

if distancia < 200:
     passagem = distancia * valorAte200
else:
    passagem = distancia * valorAcima200
    
print(f"Você vai percorrer uma distância de {distancia}km, então o preço da passagem é de R${passagem:5.2f} reais.")
# Exercício do livro Introdução à Programação com Python
# Código criado por Davi Lopes para aprendizagem  a partir de situações
# criadas no livro acima mencionado
# Nota: uma parte do código foi criado pelo autor do livro Nilo Ney Coutinho Tavares
# e adaptado por mim Davi Lopes no código estudado


pontos = 0
questão = 1

while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questão == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questão == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1
    questão = questão + 1
print(f"O aluno fez {pontos} pontos(s).")
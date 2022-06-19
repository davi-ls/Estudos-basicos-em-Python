# Velocidade do carro vs Multa

velocidade = int(input("Qual a velocidade do carro? "))

if velocidade > 80:
    print("Você foi multado.")
    multa = (velocidade - 80) * 5
    km_acima = velocidade - 80
    print(f"Sua multa é de R$ {multa:5.2f}")
    print(f"Velocidade acima do limite: {km_acima} km/h")
else:
    print("Meus parabéns por seguir o limite de velocidade.")
from datetime import date, datetime
from turtle import pd

#x = input("Digite o primeiro valor: ")
#y = input("Digite o segundo valor: ")
#print(f"A soma é: {x+y}")

#metros = int(input("Digite um valor em metros: "))
#milimetros = metros*1000
#print(f"O valor {metros} em metros é {milimetros} em milimetros")

#PROJETO PARA DESCOBRIR O TEMPO DE VIDA EM SEGUNDOS

dia_atual = (datetime.now().strftime('%d'))
mes_atual = (datetime.now().strftime('%m'))
ano_atual = (datetime.now().strftime('%y'))
data1 = datetime.date(day=22, month=11, year=2013)
print(data1)
#data_atual = datetime.date(day=dia_atual, month=mes_atual, year=ano_atual)
#print (data_atual)



data_nasc = input("Digite a data de nascimento (formato: DD/MM/AAAA):" )
hora_nasc = input("Digite a hora de nascimento (formato: 00:00:00): ")
#data_atual = (datetime.now().strftime('%d-%m-%Y'))

hora_atual = (datetime.now().strftime('%H:%M:%S'))


# print(abs((10-10-2020 - 11-12-2020).days))


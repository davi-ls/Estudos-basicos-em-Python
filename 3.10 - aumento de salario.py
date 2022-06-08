salario = int(input("Informe o salário: "))
perc = float(input("Informe a porcentagem: % "))
perc = salario * (perc/100)


aumento = salario + perc
print (f"Valor do salário com o aumento: {aumento}")

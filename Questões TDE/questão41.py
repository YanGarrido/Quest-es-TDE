# Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
Valor_da_hora = float(input("Digite o valor da hora de trabalho(em reais): "))
Num_de_horas = int(input("Digite o número de horas trabalhadas no mês: "))

Valor_pago = Valor_da_hora * Num_de_horas

Adc = Valor_pago * 0.10

Valor_recebido = Valor_pago + Adc

print(f"O valor a ser pago ao funcionário é de R${Valor_recebido}")

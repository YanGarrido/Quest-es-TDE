real = float(input("Digite um valor em real: "))
contacao_dolar = float (input("Digite a cotação do dólar: "))
valor_em_dolares = round(real/contacao_dolar, 4)
print("Valor correspondente em dólares: ", valor_em_dolares)
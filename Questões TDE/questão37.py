# Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que odesconto foi de 12%
produto = float(input("Insira o valor do seu produto: "))
desconto = produto * 0.12
valorfinal = produto - desconto
print(f"O valor do produto com um desconto de 12% é: {valorfinal}")

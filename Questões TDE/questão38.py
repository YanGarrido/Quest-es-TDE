# Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
salário = float(input("Insira o seu salário: "))
aumento = salário * 0.25
valorfinal = salário + aumento
print(f"O valor do seu salário com um aumento de 25% é: {valorfinal}")

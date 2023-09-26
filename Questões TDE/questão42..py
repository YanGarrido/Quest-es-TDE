#Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.
salario_base = float(input("Insira o salário-base de um funcionário: "))

gratificação = salario_base * 0.05

imposto = salario_base * 0.07

salario_final = (salario_base - imposto) + gratificação

print(f"O salário que o funcionário irá receber é de R${salario_final}")

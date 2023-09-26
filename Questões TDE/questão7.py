#Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A formula de conversão é: C = 5.0∗(F −32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
F = input("Digite um temperatura em Fahrenheit: ")
F = float(F)
C = 5.0*(F - 32.0)/9.0
print("A conversão da temperatura", F,"para graus Celsius é: ", C)
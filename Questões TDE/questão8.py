#Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A formula de conversão é: C = K − 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
K = input("Digite uma temperatura em graus Kelvin: ")
K = float(K)
C = K - 273.15
print("A conversão da temperatura", K,"para graus Celsius é: ", C)

#6Q Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A formula de conversão é: F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
C = input("Digite uma temperatura em graus Celsius sabendo que a  menor temperatura que o Celsius pode atingir é -273°C: ")
C = float(C)
F = C*(9.0/5.0) + 32.0
print("A conversão da temperatura", C,"para graus Fahrenheit é: ", F)
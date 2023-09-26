# Leia um valor de área em metros quadrados m2 e apresente-o convertido em acres. A formula de conversão é: A = M ∗0,000247, sendo M a área em metros quadrados e A a área em acres.
M = input("Escreva uma área em metros quadrados: ")
M = float(M)
A = M * 0.000247
input(f"Sua área em acres é: {A}")

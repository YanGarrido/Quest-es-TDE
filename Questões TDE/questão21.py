# Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é: K = L∗0,45, sendo K a massa em quilogramas e L a massa em libras.
L = input("Insira uma massa em libras: ")
L = float(L)
K = L * 0.45
print(f"A massa {L} em libras equivale a {K} quilogramas")

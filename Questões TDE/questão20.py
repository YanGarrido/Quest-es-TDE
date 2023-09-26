# Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de conversão é: L = K/0,45, sendo K a massa em quilogramas e L a massa em libras.
K = input("Insira uma massa em quilogramas: ")
K = float(K)
L = K/0.45
print(f"A massa {K} em quilogramas equivale a {L} libras")

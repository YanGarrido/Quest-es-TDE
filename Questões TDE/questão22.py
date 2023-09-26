# Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é: M = 0,91∗ J, sendo J o comprimento em jardas e M o comprimento em metros.
J = input("Digite um comprimento em jardas: ")
J = float(J)
M = 0.91 * J
print(f"O valor em metros é: {M}")

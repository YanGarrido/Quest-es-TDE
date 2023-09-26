# Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.
C = float(input("Digite o comprimento do terreno (em metros): "))
L = float(input("Digite a largura do terreno (em metros): "))
P = float(input("Digite o preço do metro de tela (em reais por metro): "))

Perimetro = (C * 2) + (L * 2)
Custo = P * Perimetro

print(f"O custo para cercar o terreno é de R${Custo}")

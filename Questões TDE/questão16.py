#Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. A formula de conversão é: C = P ∗2,54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
P = input("Escreva um comprimento em polegadas:")
P = float(P)
C = P * 2.54
print("A converção do comprimento", P,"em polegadas para centímetros é: ", C)

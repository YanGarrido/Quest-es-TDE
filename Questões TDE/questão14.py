#Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G ∗ π/180, sendo G o angulo em graus e R em radianos e π = 3.14.
G = input("Escreva um ângulo em graus: ")
G = float(G)
R = G * 3.14/180
print("A converção do ângulo", G,"em graus para radianos é: ", R)

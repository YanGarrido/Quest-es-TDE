#Leia um angulo em radianos e apresente-o convertido em graus. A fórmula de conversão é: G = R ∗180/π, sendo G o angulo em graus e R em radianos e π = 3.14.
R = input("Escreva um ângulo em radianos:")
R = float(R)
G = R * 180/3.14
print("A converção do ângulo", R,"em radianos para graus é: ", G)
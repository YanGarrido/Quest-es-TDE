import math


def calcular_distancia_origem(x, y):

    distancia = math.sqrt(x**2 + y**2)
    return distancia


x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

distancia_origem = calcular_distancia_origem(x, y)

print("A distância da origem é:", distancia_origem)

import math


def calcular_quantidade_degraus(altura_desejada, altura_degrau):

    return math.ceil(altura_desejada / altura_degrau)


altura_degrau = float(
    input("Digite a altura de cada degrau (em centímetros): "))
altura_desejada = float(
    input("Digite a altura que deseja alcançar (em centímetros): "))


altura_degrau_cm = altura_degrau
altura_desejada_cm = altura_desejada


quantidade_degraus = calcular_quantidade_degraus(
    altura_desejada_cm, altura_degrau_cm)


print("Você precisará subir", quantidade_degraus,
      "degraus para atingir sua altura desejada.")

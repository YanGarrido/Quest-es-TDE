def calcular_participacao(valor_investido, total_investido, premio):
    return (valor_investido / total_investido) * premio


investimento_apostador1 = float(
    input("Informe o valor investido pelo primeiro apostador: "))
investimento_apostador2 = float(
    input("Informe o valor investido pelo segundo apostador: "))
investimento_apostador3 = float(
    input("Informe o valor investido pelo terceiro apostador: "))

total_investido = investimento_apostador1 + \
    investimento_apostador2 + investimento_apostador3

premio = float(input("Informe o valor do prêmio: "))

participacao_apostador1 = calcular_participacao(
    investimento_apostador1, total_investido, premio)
participacao_apostador2 = calcular_participacao(
    investimento_apostador2, total_investido, premio)
participacao_apostador3 = calcular_participacao(
    investimento_apostador3, total_investido, premio)

print("Quantidade que cada apostador ganharia do prêmio:")
print("Apostador 1: R$", round(participacao_apostador1, 2))
print("Apostador 2: R$", round(participacao_apostador2, 2))
print("Apostador 3: R$", round(participacao_apostador3, 2))

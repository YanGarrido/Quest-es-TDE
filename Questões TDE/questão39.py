# A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
# • O primeiro ganhador receberá 46%;
# • O segundo recebera 32%;
# • O terceiro recebera o restante;
# Calcule e imprima a quantia ganha por cada um dos ganhadores.
print("A quantia ganha por cada um dos ganhadores foi:")
firstwinner = 780000 * 0.46
print(f"O primeiro ganhador faturou a quantia de R${firstwinner}")
secondwinner = 780000 * 0.32
print(f"O segundo ganhador faturou a quantia de R${secondwinner}")
thirdwinner = 780000 - (firstwinner + secondwinner)
print(f"O terceiro ganhador faturou a quantia de R${thirdwinner}")

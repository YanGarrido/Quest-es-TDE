def inverter_digitos(numero):

    numero_invertido = str(numero)[::-1]

    numero_invertido = int(numero_invertido)
    return numero_invertido


numero = int(
    input("Digite um número inteiro de três dígitos (entre 100 e 999): "))


if 100 <= numero <= 999:

    numero_invertido = inverter_digitos(numero)

    print("O número com os dígitos invertidos é:", numero_invertido)
else:
    print("Por favor, digite um número de três dígitos (entre 100 e 999).")

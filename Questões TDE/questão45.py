def converter_maiuscula_para_minuscula(letra_maiuscula):

    if ord('A') <= ord(letra_maiuscula) <= ord('Z'):

        letra_minuscula = chr(ord(letra_maiuscula) + 32)
        return letra_minuscula
    else:
        return "Por favor, insira uma letra maiúscula."


letra_maiuscula = input("Digite uma letra maiúscula: ")


letra_minuscula = converter_maiuscula_para_minuscula(letra_maiuscula)


print("A letra minúscula correspondente é:", letra_minuscula)

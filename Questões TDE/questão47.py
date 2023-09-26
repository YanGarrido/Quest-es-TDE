numero_digitado = int(input('Digite um número de 1000 à 9999: '))


if int(numero_digitado) >= 1000 and int(numero_digitado) <= 9999:

   linhas = str(numero_digitado)

   print(str(linhas[0]))

   print(str(linhas[1]))

   print(str(linhas[2]))

   print(str(linhas[3]))

else:

   print('Número invalido')
#Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em litros. A formula de conversão é: L = 1000∗ M, sendo L o volume em litros e M o volume em metros cúbicos.
M = input("Escreva um volume: ")
M = float(M)
L = 1000 * M
print("O volume", M," equivale a", L," litros")
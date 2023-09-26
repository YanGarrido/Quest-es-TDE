#Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3. A formula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros cúbicos.
L = input("Escreva um volume em litros: ")
L = float(L)
M = L/1000
print(f"O volume {M} equivale a {L} litros")
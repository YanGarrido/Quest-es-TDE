# Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
dia = int(input("Insira o número de dias que o encanador vai trabalhar: "))

quant_semimposto = 30 * dia
imposto = quant_semimposto * 0.08
quant_liquida = quant_semimposto - imposto

print(
    f"O valor que deverá ser pago para o encanador será de R${quant_liquida}")

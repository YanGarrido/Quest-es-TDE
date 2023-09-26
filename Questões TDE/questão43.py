def calcular_desconto(valor_total):

    return valor_total * 0.9


def calcular_valor_parcela(valor_total, num_parcelas):

    return valor_total / num_parcelas


def calcular_comissao_a_vista(valor_com_desconto):

    return valor_com_desconto * 0.05


def calcular_comissao_parcelada(valor_total):

    return valor_total * 0.05


valor_total = float(input("Digite o valor total da venda: "))


valor_com_desconto = calcular_desconto(valor_total)


valor_parcela = calcular_valor_parcela(valor_total, 3)


comissao_a_vista = calcular_comissao_a_vista(valor_com_desconto)


comissao_parcelada = calcular_comissao_parcelada(valor_total)


print("Total a pagar com desconto de 10%:", valor_com_desconto)
print("Valor de cada parcela (3x sem juros):", valor_parcela)
print("Comissão do vendedor (venda à vista):", comissao_a_vista)
print("Comissão do vendedor (venda parcelada):", comissao_parcelada)

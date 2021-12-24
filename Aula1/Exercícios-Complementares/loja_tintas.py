'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
tinta a serem compradas e o preço total.
Obs.: somente são vendidos um número inteiro de latas.
'''

import math
tamanho_mq = float(input('Informe o tamanho em metros quadrados da área a ser pintada:'))
metro_lata = 18 * 3
#função da biblioteca math para sempre arredondar para o próximo número inteiro
quant_latas = math.ceil(tamanho_mq / metro_lata)
preco = round(quant_latas * 80, 2)
print(f'Você vai precisar de {quant_latas} lata(s)')
print(f'Preço: R${preco}')
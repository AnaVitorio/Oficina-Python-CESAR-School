#11.Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
# O produto do dobro do primeiro com metade do segundo.
# Soma do triplo do primeiro com o terceiro.
# Terceiro elevado ao cubo.

inteiro1 = int(input('Digite um número inteiro:'))
inteiro2 = int(input('Digite outro número inteiro:'))
real = float(input('Digite um número real:'))

produto = (inteiro1 * 2) * (inteiro2 / 2)
soma = (inteiro1 * 3) + real
cubo = real**3
print(f'O produto do dobro do primeiro com metade do segundo é {produto}')
print(f'A soma do triplo do primeiro com o terceiro é {soma}')
print(f'O terceiro elevado ao cubo é {cubo}')
